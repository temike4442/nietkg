from django.urls import path
from .views import ListAd,DetailAd

urlpatterns=[
    path('',ListAd.as_view()),
    path('detail/<int:pk>/',DetailAd.as_view()),
]