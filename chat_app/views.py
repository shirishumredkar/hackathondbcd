import os
import json
from typing import TypedDict, Literal
from django.shortcuts import render
from django.http import Http404, FileResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.conf import settings

from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langgraph.graph import StateGraph, START, END
from .models import ChatMessage


# --- 1. Thread-Safe Global State Mapping Blueprint ---
class GraphState(TypedDict):
    question: str
    retrieved_context: str
    answer: str
    score: float


# Initialize Embedding Reference to link search queries with compiled indices
embedding_model = OpenAIEmbeddings(
    base_url=settings.ENDPOINT,
    api_key=settings.GITHUB_TOKEN,
    model=settings.EMBEDDING_MODEL_NAME
)
vectorstore = Chroma(persist_directory=settings.CHROMA_DB_PATH, embedding_function=embedding_model)


# --- 2. LangGraph Execution Node Nodes ---
def retrieve_node(state: GraphState) -> dict:
    question = state["question"]
    results = vectorstore.similarity_search_with_score(question, k=1)

    if not results:
        print(f"[Hotscan Debug] -> Zero database records found for query: '{question}'")
        return {"retrieved_context": "", "score": 999.0}

    doc, score = results[0]
    print(f"[Hotscan Debug] -> Closest Match Snippet: '{doc.page_content}' | Chroma Distance Score: {score:.4f}")
    return {"retrieved_context": doc.page_content, "score": float(score)}


def generate_answer_node(state: GraphState) -> dict:
    retrieved_context = state["retrieved_context"]
    question = state["question"]

    print(f"[Hotscan Debug] -> Forwarding to LLM Node ({settings.MODEL_NAME})...")
    prompt = f"""You are a strict assistant.
Answer ONLY from provided context.
If Answer is not present in context, reply exactly:
I don't know answer

Context:
{retrieved_context}

Question:
{question}"""

    client = OpenAI(base_url=settings.ENDPOINT, api_key=settings.GITHUB_TOKEN)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=settings.MODEL_NAME,
        temperature=0,
        max_completion_tokens=100
    )
    answer = response.choices[0].message.content
    print(f"[Hotscan Debug] -> LLM Engine Response Output: '{answer}'")
    return {"answer": answer}


def generate_no_answer_node(state: GraphState) -> dict:
    print("[Hotscan Debug] -> Distance exceeded safety threshold. Routing to Fallback No-Answer Node.")
    return {"answer": "I don't know answer"}


# --- 3. Dynamic Conditional Router Edges ---
def should_generate(state: GraphState) -> Literal["generate", "no_answer"]:
    score = state["score"]

    # CRITICAL CHROMADB FIX: High distance score means LESS relevant.
    # Route to no_answer ONLY IF distance score is higher than our limit.
    if score > settings.THRESHOLD_SCORE:
        return "no_answer"
    return "generate"


# --- 4. Graph Construction & Compilation Sequence ---
graph = StateGraph(GraphState)
graph.add_node("retrieve", retrieve_node)
graph.add_node("generate", generate_answer_node)
graph.add_node("no_answer", generate_no_answer_node)

graph.add_edge(START, "retrieve")
graph.add_conditional_edges(
    source="retrieve",
    path=should_generate,
    path_map={"generate": "generate", "no_answer": "no_answer"}
)
graph.add_edge("generate", END)
graph.add_edge("no_answer", END)
graph_compiled = graph.compile()


# --- 5. Django Core Application View Controllers ---
@login_required
def chatbot_view(request):
    history = ChatMessage.objects.filter(user=request.user)
    return render(request, 'chatbot.html', {'chat_history': history})


@login_required
@require_POST
def chatbot_api(request):
    """Processes real-time UI text interactions across the compiled LangGraph setup"""
    try:
        data = json.loads(request.body)
        user_msg = data.get('message', '').strip()
        if not user_msg:
            return JsonResponse({'error': 'Message content parameters empty.'}, status=400)

        # A. Log current human user interaction text
        ChatMessage.objects.create(user=request.user, role='user', text=user_msg)

        # B. Run context validation across compiled Graph
        graph_output = graph_compiled.invoke({"question": user_msg})
        bot_reply_text = graph_output.get("answer", "I don't know answer")

        # C. Log generated system model outcome response
        ChatMessage.objects.create(user=request.user, role='bot', text=bot_reply_text)

        return JsonResponse({'status': 'success', 'reply': bot_reply_text})
    except Exception as e:
        print(f"[Hotscan Severe Critical Error]: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def downloads_view(request):
    return render(request, 'downloads.html')


@login_required
def download_file_backend(request, filename):
    protected_directory = os.path.join(settings.BASE_DIR, 'protected_files')
    target_path = os.path.abspath(os.path.join(protected_directory, filename))
    if not target_path.startswith(protected_directory):
        raise Http404("Unauthorized path lookup access restriction.")
    if os.path.exists(target_path) and os.path.isfile(target_path):
        return FileResponse(open(target_path, 'rb'), as_attachment=True)
    raise Http404("File parameter missing from server mapping records.")
