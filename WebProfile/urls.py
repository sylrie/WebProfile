"""WebProfile URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from WebProfile import settings

from django.contrib.sitemaps.views import sitemap
from webapp.sitemaps import Static_Sitemap

sitemaps = {
    'static': Static_Sitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('', include('SRD.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
