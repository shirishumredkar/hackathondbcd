import os
from pathlib import Path
from dotenv import load_dotenv

# 1. ALWAYS LOAD ENVIRONMENT VARIABLES FIRST
# This fixes the LangChain startup connection error by placing keys in memory immediately.
BASE_DIR = Path(__file__).resolve().parent.parent
gcp_secret_path = "/app/secrets/.env"
if os.path.exists(gcp_secret_path):
    load_dotenv(gcp_secret_path)
else:
    load_dotenv(os.path.join(BASE_DIR, '.env'))

# --- SECURE CONFIGURATIONS FROM ENVIRONMENT ---
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-dev-token-professional-ui')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() in ('true', '1', 't')

# Explicitly trust the Cloud Run origin for secure POST requests (Include https://)
CSRF_TRUSTED_ORIGINS = [
    'https://run.app',
]

# ALLOWED_HOSTS must include '*' or your Cloud Run domain for the app to be reachable online
ALLOWED_HOSTS = [    'cloudrun-app-server-272907652960.us-central1.run.app',
    'localhost',
    '127.0.0.1',]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat_app',  # Connects your application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Tells Django where HTML files are
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security routing configurations
LOGIN_REDIRECT_URL = 'chatbot'
LOGOUT_REDIRECT_URL = 'login'

# --- REFRACTORED AI MODEL CONFIGURATIONS ---
# If GITHUB_AI_TOKEN isn't in your .env, it defaults to the working empty string "".
GITHUB_TOKEN = os.environ.get('GITHUB_AI_TOKEN', '')
ENDPOINT = "https://models.github.ai/inference"
MODEL_NAME = "openai/gpt-4o-mini"
EMBEDDING_MODEL_NAME = "text-embedding-3-small"
THRESHOLD_SCORE = 1.5

# Absolute Server Directory Layout Profiles
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')
DATABASE_DIR = os.path.join(BASE_DIR, 'database')

INTERNAL_FILE_PATH = os.path.join(DATASET_DIR, 'profile.txt')
CHROMA_DB_PATH = os.path.join(DATABASE_DIR, 'db')

# Ensure directories physically exist on startup
os.makedirs(DATASET_DIR, exist_ok=True)
os.makedirs(DATABASE_DIR, exist_ok=True)
