from django.urls import path,include
from .views import ListAd,DetailAd


urlpatterns=[
    path('',ListAd.as_view()),
    path('detail/<int:pk>/',DetailAd.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]