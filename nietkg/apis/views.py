from rest_framework import generics,filters
from django.shortcuts import render
from doska import models
from rest_framework.permissions import IsAuthenticated

from .serializers import AdReadSerializer,AdWriteSerializer,RegionSerializer,CategorySerializer,ValuteSerializer
from rest_framework import permissions

class ListAd(generics.ListAPIView):
    queryset=models.Ad.objects.all().order_by('-pk')[:50]
    serializer_class=AdReadSerializer

class DetailAd(generics.RetrieveAPIView):
    serializer_class = AdReadSerializer
    queryset = models.Ad.objects.all()

class CreateAd(generics.ListCreateAPIView):
    queryset=models.Ad.objects.all()[:2]
    serializer_class=AdWriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save()

class CategoryAd(generics.ListAPIView):
    serializer_class = AdReadSerializer

    def get_queryset(self):
        cat_id=self.kwargs['id']
        return models.Ad.objects.filter(category=cat_id)

class SearchAd(generics.ListCreateAPIView):
    serializer_class = AdReadSerializer

    def get_queryset(self):
        queryset = models.Ad.objects.filter(title__icontains=self.kwargs['search_text'])
        return queryset

class RegionAd(generics.ListAPIView):
    serializer_class = AdReadSerializer

    def get_queryset(self):
        reg_id=self.kwargs['id']
        return models.Ad.objects.filter(region=reg_id)

class Regions(generics.ListAPIView):
    serializer_class = RegionSerializer
    queryset = models.Region.objects.all()

class Categories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = models.Category.objects.all()

class Valutes(generics.ListAPIView):
    serializer_class = ValuteSerializer
    queryset = models.Valute.objects.all()
'''class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = "__all__"

class CafeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Cafe
      fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)
  cade = CafeSerializer(read_only=True)
  class Meta:
    model = Category
    fields = ['name', 'user', 'cafe']'''

