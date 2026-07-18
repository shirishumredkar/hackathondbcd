from django.apps import AppConfig


import os
from django.apps import AppConfig
from django.conf import settings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

class ChatAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat_app'

    def ready(self):
        # Prevent double-execution when Django runs the reload checker thread
        if os.environ.get('RUN_MAIN') != 'true':
            return

        # 1. Output profile lines dataset target parameters
        lines = [
            "My name is Shirish Umredkar\n",
            "My age is 43\n",
            "My organization is Deutsche Bank\n",
            "My favourite movie is Interstellar\n",
            "My favourite destination for vacation is Vietnam\n"
        ]

        with open(settings.INTERNAL_FILE_PATH, "w", encoding="utf-8") as file:
            file.writelines(lines)
        print("[Hotscan Ingestion]: Profile dataset written successfully.")

        # 2. Extract context structures out of memory paths
        with open(settings.INTERNAL_FILE_PATH, "r", encoding="utf-8") as f:
            text_profile = f.read()

        # 3. Chunk structural strings
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
        text_chunks = text_splitter.split_text(text_profile)

        # 4. Global Embeddings Initialization
        embedding_model = OpenAIEmbeddings(
            base_url=settings.ENDPOINT,
            api_key=settings.GITHUB_TOKEN,
            model=settings.EMBEDDING_MODEL_NAME,
            tiktoken_enabled=False
        )

        # 5. Build and populate Chroma Vector Store
        # We reuse the active database instance across runs
        global_vectorstore = Chroma.from_texts(
            texts=text_chunks,
            embedding=embedding_model,
            persist_directory=settings.CHROMA_DB_PATH
        )
        print(f"[Hotscan Ingestion]: Vector database instantiated at {settings.CHROMA_DB_PATH}")
