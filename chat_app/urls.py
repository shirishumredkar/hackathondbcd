from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chatbot_view, name='chatbot'),
    path('chat/api/', views.chatbot_api, name='chatbot_api'),
    path('downloads/', views.downloads_view, name='downloads'),
    path('downloads/file/<str:filename>/', views.download_file_backend, name='download_file'),
]
