from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),  # Injected default login mechanisms
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('chat_app.urls')),
    path('', RedirectView.as_view(url='chat/', permanent=False)),
]

