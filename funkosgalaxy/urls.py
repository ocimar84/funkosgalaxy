"""
URL configuration for funkosgalaxy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# No arquivo urls.py do diretório "funkosgalaxy"

from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    # URLs do painel de administração
    path('admin/', admin.site.urls),
    
    # Redirecionar para a página inicial da store
    path('', lambda request: redirect('/store/')),
    
    # Incluir as URLs do aplicativo 'store'
    path('store/', include('funkosgalaxy.store.urls')),
]

