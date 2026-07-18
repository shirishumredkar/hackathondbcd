
import re

# Read requirements.txt content
requirements_content = """aiohappyeyeballs==2.4.2
aiohttp==3.10.8
aiosignal==1.3.1
altair==6.1.0
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.13.0
apache-airflow==2.10.2
apache-airflow-providers-common-compat==1.2.0
apache-airflow-providers-common-io==1.4.1
apache-airflow-providers-common-sql==1.17.0
apache-airflow-providers-fab==1.4.0
apache-airflow-providers-ftp==3.11.1
apache-airflow-providers-http==4.13.1
apache-airflow-providers-imap==3.7.0
apache-airflow-providers-smtp==1.8.0
apache-airflow-providers-sqlite==3.9.0
apispec==6.6.1
argcomplete==3.5.0
argon2-cffi==25.1.0
argon2-cffi-bindings==25.1.0
arrow==1.4.0
asgiref==3.11.1
asttokens==3.0.1
async-lru==2.3.0
attrs==26.1.0
babel==2.18.0
bcrypt==5.0.0
beautifulsoup4==4.14.3
bleach==6.3.0
blinker==1.9.0
build==1.5.0
cachelib==0.9.0
cachetools==7.1.2
certifi==2026.4.22
cffi==2.0.0
charset-normalizer==3.4.7
chromadb==1.5.9
click==8.4.0
clickclick==20.10.2
colorama==0.4.6
colorlog==6.8.2
comm==0.2.3
connexion==2.14.2
cron-descriptor==1.4.5
croniter==3.0.3
cryptography==49.0.0
debugpy==1.8.20
decorator==5.2.1
defusedxml==0.7.1
Deprecated==1.2.14
dill==0.3.9
distro==1.9.0
Django==6.0.6
django-environ==0.14.0
django-storages==1.14.6
djangorestframework==3.17.1
djangorestframework_simplejwt==5.5.1
djoser==2.3.3
dnspython==2.6.1
docutils==0.21.2
dotenv==0.9.9
durationpy==0.10
email_validator==2.2.0
executing==2.2.1
fastcore==1.13.2
fastjsonschema==2.21.2
filelock==3.29.0
Flask==2.2.5
Flask-AppBuilder==4.5.0
Flask-Babel==2.0.0
Flask-Caching==2.3.0
Flask-JWT-Extended==4.6.0
Flask-Limiter==3.8.0
Flask-Login==0.6.3
Flask-Session==0.5.0
Flask-WTF==1.2.1
flatbuffers==25.12.19
fqdn==1.5.1
frozenlist==1.4.1
fsspec==2024.9.0
gitdb==4.0.12
GitPython==3.1.50
google-api-core==2.32.0
google-auth==2.56.0
google-cloud-core==2.6.0
google-cloud-storage==3.13.0
google-crc32c==1.8.0
google-re2==1.1.20240702
google-resumable-media==2.10.0
googleapis-common-protos==1.65.0
grpcio==1.66.2
gunicorn==23.0.0
h11==0.16.0
hf-xet==1.5.0
httpcore==1.0.9
httptools==0.7.1
httpx==0.28.1
huggingface_hub==1.15.0
idna==3.15
importlib_metadata==8.4.0
importlib_resources==6.4.5
inflection==0.5.1
ipykernel==7.2.0
ipython==9.13.0
ipython_pygments_lexers==1.1.1
ipywidgets==8.1.8
isoduration==20.11.0
itsdangerous==2.2.0
jedi==0.20.0
Jinja2==3.1.6
jiter==0.14.0
jmespath==1.0.1
json5==0.14.0
jsonpatch==1.33
jsonpointer==3.1.1
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
jupyter==1.1.1
jupyter-console==6.6.3
jupyter-events==0.12.1
jupyter-lsp==2.3.1
jupyter_client==8.8.0
jupyter_core==5.9.1
jupyter_server==2.18.2
jupyter_server_terminals==0.5.4
jupyterlab==4.5.7
jupyterlab_pygments==0.3.0
jupyterlab_server==2.28.0
jupyterlab_widgets==3.0.16
kubernetes==35.0.0
langchain-chroma==1.1.0
langchain-core==1.4.0
langchain-openai==1.2.1
langchain-protocol==0.0.15
langchain-text-splitters==1.1.2
langgraph==1.2.0
langgraph-checkpoint==4.1.0
langgraph-prebuilt==1.1.0
langgraph-sdk==0.3.14
langsmith==0.8.5
lark==1.3.1
lazy-object-proxy==1.10.0
limits==3.13.0
linkify-it-py==2.0.3
lockfile==0.12.2
markdown-it-py
MarkupSafe==3.0.3
marshmallow==3.22.0
marshmallow-oneofschema==3.1.1
marshmallow-sqlalchemy==0.28.2
matplotlib-inline==0.2.2
mdit-py-plugins==0.4.2
mdurl==0.1.2
methodtools==0.4.7
mistune==3.2.1
mmh3==5.2.1
multidict==6.1.0
narwhals==2.21.2
nbclient==0.10.4
nbconvert==7.17.1
nbformat==5.10.4
nest-asyncio==1.6.0
notebook==7.5.6
notebook_shim==0.2.4
numpy==2.4.5
oauthlib==3.3.1
onnxruntime==1.26.0
openai==2.37.0
opentelemetry-api==1.27.0
opentelemetry-exporter-otlp==1.27.0
opentelemetry-exporter-otlp-proto-common==1.27.0
opentelemetry-exporter-otlp-proto-grpc==1.27.0
opentelemetry-exporter-otlp-proto-http==1.27.0
opentelemetry-proto==1.27.0
opentelemetry-sdk==1.27.0
opentelemetry-semantic-conventions==0.48b0
oredered-set==4.1.0
orjson==3.11.9
ormsgpack==1.12.2
overrides==7.7.0
packaging
pandas==3.0.3
pandocfilters==1.5.1
parso==0.8.7
pathspec==0.12.1
pendulum==3.0.0
pillow==12.2.0
platformdirs==4.9.6
prison==0.2.1
prometheus_client==0.25.0
prompt_toolkit==3.0.52
proto-plus==1.28.1
protobuf
psutil==7.2.2
pure_eval==0.2.3
pyarrow==24.0.0
pyasn1==0.6.4
pyasn1_modules==0.4.2
pybase64==1.4.3
pycparser==3.0
pydantic==2.13.4
pydantic-settings==2.14.1
pydantic_core==2.46.4
pydeck==0.9.2
Pygments==2.20.0
PyJWT==2.13.0
PyPika==0.51.1
pyproject_hooks==1.2.0
python-daemon==3.0.1
python-dateutil==2.9.0.post0
python-dotenv==1.2.2
python-json-logger==4.1.0
python-multipart==0.0.28
python-nvd3==0.16.0
python3-openid==3.2.0
pywinpty==3.0.3
PyYAML==6.0.3
pyzmq==27.1.0
referencing==0.37.0
regex==2026.5.9
requests==2.34.2
requests-oauthlib==2.0.0
requests-toolbelt==1.0.0
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rfc3987-syntax==1.1.0
rich
rich-argparse==1.5.2
rpds-py==0.30.0
Send2Trash==2.1.0
setproctitle==1.3.3
setuptools==82.0.1
shellingham==1.5.4
six==1.17.0
smmap==5.0.3
sniffio==1.3.1
social-auth-app-django==5.9.0
social-auth-core==4.9.1
soupsieve==2.8.3
SQLAlchemy==1.4.54
SQLAlchemy-JSONField==1.0.2
SQLAlchemy-Utils==0.41.2
sqlparse==0.5.1
stack-data==0.6.3
starlette==1.0.0
stqdm==0.0.5
streamlit==1.57.0
streamlit-jupyter==0.3.1
tabulate==0.9.0
tenacity==9.0.0
termcolor==2.4.0
terminado==0.18.1
tiktoken==0.13.0
time-machine==2.15.0
tinycss2==1.4.0
tokenizers==0.23.1
toml==0.10.2
tornado==6.5.5
tqdm==4.67.3
traitlets==5.15.0
typer==0.25.1
typing-inspection==0.4.2
typing_extensions==4.15.0
tzdata==2024.2
uc-micro-py==1.0.3
unicodecsv==0.14.1
universal_pathlib==0.2.5
uri-template==1.3.0
urllib3==2.7.0
uuid_utils==0.15.0
uvicorn==0.47.0
watchdog==6.0.0
watchfiles==1.1.1
wcwidth==0.7.0
webcolors==25.10.0
webencodings==0.5.1
websocket-client==1.9.0
websockets==16.0
Werkzeug==2.2.3
wheel==0.46.3
widgetsnbextension==4.0.15
wirerope==0.4.7
wrapt==1.16.0
WTForms==3.1.2
xxhash==3.7.0
yarl==1.13.1
zipp==3.20.2
zstandard==0.25.0
environ
"""

# Parse requirements.txt
package_versions = {}
for line in requirements_content.splitlines():
    line = line.strip()
    if line and not line.startswith('#'):
        match = re.match(r'([\w\d\-\_.]+)(==|>=|<=|~=|=<|=>)([\d\.]+)', line)
        if match:
            package = match.group(1)
            version = match.group(3)
            package_versions[package.replace('-', '_')] = version
        else:
            package_versions[line.replace('-', '_')] = "N/A" # No version specified

# Grep output of import statements
grep_output = """D:/Hackathon/ui\\manage.py
3:import os
4:import sys
D:/Hackathon/ui\\myproject\\asgi.py
10:import os
D:/Hackathon/ui\\myproject\\settings.py
1:import os
2:import environ
10:from pathlib import Path
D:/Hackathon/ui\\chat_app\\apps.py
3:import os
5:from langchain_text_splitters import RecursiveCharacterTextSplitter
6:from langchain_openai import OpenAIEmbeddings
7:from langchain_chroma import Chroma
D:/Hackathon/ui\\myproject\\wsgi.py
10:import os
D:/Hackathon/ui\\chat_app\\migrations\\0001_initial.py
3:import django.db.models.deletion
D:/Hackathon/ui\\chat_app\\views.py
1:import os
2:import json
3:from typing import TypedDict, Literal
11:from openai import OpenAI
12:from langchain_openai import OpenAIEmbeddings
13:from langchain_chroma import Chroma"""

# Extract imported packages
imported_packages = set()
for line in grep_output.splitlines():
    import_match = re.search(r'(?:import|from)\s+([\w\d_.]+)', line)
    if import_match:
        full_package_name = import_match.group(1)
        # Take the top-level package name
        top_level_package = full_package_name.split('.')[0]
        imported_packages.add(top_level_package.replace('-', '_'))

# Special handling for common packages that might not be in requirements.txt
# but are built-in or implicitly available (e.g., os, sys, json, typing, pathlib)
# and for packages that have different import names vs. package names
# (e.g., django.db.models.deletion -> Django)

# Add known built-in modules
built_in_modules = {'os', 'sys', 'json', 'typing', 'pathlib'}
imported_packages = imported_packages - built_in_modules

# Handle specific package name mappings
if 'django' in imported_packages:
    imported_packages.remove('django')
    imported_packages.add('Django')
if 'environ' in imported_packages:
    imported_packages.remove('environ')
    imported_packages.add('django_environ')
if 'openai' in imported_packages:
    imported_packages.remove('openai')
    imported_packages.add('openai') # It's already 'openai', but keeping this pattern for consistency
if 'langchain_text_splitters' in imported_packages:
    imported_packages.remove('langchain_text_splitters')
    imported_packages.add('langchain_text_splitters')
if 'langchain_openai' in imported_packages:
    imported_packages.remove('langchain_openai')
    imported_packages.add('langchain_openai')
if 'langchain_chroma' in imported_packages:
    imported_packages.remove('langchain_chroma')
    imported_packages.add('langchain_chroma')


# Compile the final list
result = []
for pkg in sorted(list(imported_packages)):
    version = package_versions.get(pkg, "Not found in requirements.txt or version not specified")
    result.append(f"{pkg}: {version}")

print("\\n".join(result))
