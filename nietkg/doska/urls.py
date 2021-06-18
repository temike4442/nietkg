import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .models import *
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('add/',add_new,name='add'),
]

if settings.DEBUG:
      urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)