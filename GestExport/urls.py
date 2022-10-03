"""GestExport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from profiles.urls import profiles_patterns
from django.conf import settings


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    # Path de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Path de Profiles
    path('profiles/', include(profiles_patterns)),
    # path del Pages
    path('page/', include('pages.urls')),
    # path del Tables Générales
    path('tables/', include('tables.urls', namespace='tables')),
    # path de Betou 
    path('betou/', include('betou.urls', namespace='betou')),
    # path de Douala 
    path('douala/', include('douala.urls', namespace='douala')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Custom titiles for admin
admin.site.site_header = "GestExport"
admin.site.index_title = "Panneau d'Administration"
admin.site.site_title = "GestExport"
