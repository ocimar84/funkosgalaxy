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
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView 
from store.sitemap import ProductSitemap

sitemaps = {
    'product': ProductSitemap,
}

urlpatterns = [
    path('', include('store.urls')),
    # URLs do painel de administração
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path("robots.txt",TemplateView.as_view(template_name="seo/robots.txt", content_type="text/plain")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'store.views.error_404_view'
handler400 = 'store.views.error_400_view'
handler403 = 'store.views.error_403_view'
handler500 = 'store.views.error_500_view'