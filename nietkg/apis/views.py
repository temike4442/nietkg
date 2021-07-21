from rest_framework import generics
from django.shortcuts import render
from doska import models
from .serializers import AdSerializer

class ListAd(generics.ListCreateAPIView):
    queryset=models.Ad.objects.all()
    serializer_class=AdSerializer

class DetailAd(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        pk=self.kwargs['pk']
        return models.Ad.objects.filter(pk=pk)
