from django.contrib import admin
from django.urls import path,include
from .models import *
from .views import *

urlpatterns = [
    path('',index,name='home')
]