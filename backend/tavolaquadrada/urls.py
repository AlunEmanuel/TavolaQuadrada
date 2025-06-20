"""
URL configuration for tavolaquadrada project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# backend/tavolaquadrada/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Web.views import ItemViewSet
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
import os

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Serve o index.html do frontend Angular para qualquer rota não-API
    path('', TemplateView.as_view(template_name='index.html'), name='frontend'),
]

# Serve arquivos estáticos do Angular (build) em produção
if settings.DEBUG is False:
    urlpatterns += [
        path('static/<path:path>', serve, {'document_root': os.path.join(settings.BASE_DIR, 'static')}),
    ]