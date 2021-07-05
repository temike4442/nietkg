import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .models import *
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('ad/<int:pk>',AdView.as_view(),name='ad_detail'),
    path('add/',add_new,name='add'),
    path('search/',AdSearchView.as_view(),name='search'),
    path('category/<int:pk>',AdCategoryView.as_view(),name='category'),
    #path('category/<int:pk>/search/',SearchCategoryView.as_view(),name='category_search'),
    path('categories/',AllCategories.as_view(),name='all_categories'),

]


if settings.DEBUG:
      urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)