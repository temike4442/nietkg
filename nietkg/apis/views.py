from rest_framework import generics
from django.shortcuts import render
from doska import models
from .serializers import AdSerializer
from rest_framework import permissions

class ListAd(generics.ListCreateAPIView):
    queryset=models.Ad.objects.all().order_by('-pk')#[:2]
    serializer_class=AdSerializer

class DetailAd(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdSerializer
    queryset = models.Ad.objects.all()
    #def get_queryset(self):
     #   pk=self.kwargs['pk']
      #  return models.Ad.objects.filter(pk=pk)

