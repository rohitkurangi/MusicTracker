"""MusicPlayer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from django.views.generic import TemplateView
from crud_ajax.views import CrudView, CreateCrudUser, DeleteCrudUser, UpdateCrudUser, TrackMusic,NextPreviousTracks
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include("catalogue.urls")),
    path('crud/', CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('tracks/', TrackMusic.as_view(), name='tracks'),
    path('tracks/<str:event>\w+/<str:priority>\w+/', NextPreviousTracks.as_view(), name='tracks'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


