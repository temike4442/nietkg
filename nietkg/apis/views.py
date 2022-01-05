from rest_framework import generics
from doska import models
from rest_framework.response import Response
from .service import PaginationAds
from .serializers import AdReadSerializer, AdWriteSerializer, RegionSerializer, CategorySerializer, ValuteSerializer, \
    StorySerializer

class ListAd(generics.ListAPIView):
    queryset=models.Ad.objects.all().order_by('-pk')[:200]
    serializer_class=AdReadSerializer
    pagination_class = PaginationAds

class DetailAd(generics.RetrieveAPIView):
    serializer_class = AdReadSerializer
    queryset = models.Ad.objects.all()
    pagination_class = None

class CreateAd(generics.ListCreateAPIView):
    queryset=models.Ad.objects.all()[:2]
    serializer_class=AdWriteSerializer
    pagination_class = None
    http_method_names = ['post','delete','get','put']

    def create(self, request, *args, **kwargs):
        print(request.data)
        images = request.FILES.getlist('images')
        print(images)
        cat_id = models.Category.objects.get(pk=request.data['category'])
        region_id = models.Region.objects.get(pk=request.data['region'])
        valute_id = models.Valute.objects.get(pk=request.data['valute'])
        ad_id=models.Ad.objects.create(title=request.data['title'],content=request.data['content'],number=request.data['number'],
        name=request.data['name'],address=request.data['address'],price=request.data['price'],views=request.data['views'],
        is_active=request.data['is_active'],category=cat_id,region=region_id,valute=valute_id)
        for image in images:
            print(str(image)+' rrrrrrrrrrr')
            models.Images.objects.create(ad=ad_id,image=image)
        return Response(data=ad_id.id)

class CategoryAd(generics.ListAPIView):
    serializer_class = AdReadSerializer
    pagination_class = PaginationAds

    def get_queryset(self):
        category=self.kwargs['id']
        region=self.kwargs['region']
        if category == 999 and region == 999:
            queryset = models.Ad.objects.all()[:200]
        if category == 999 and region != 999:
            queryset = models.Ad.objects.filter(region=region)[:200]
        if category != 999 and region == 999:
            queryset = models.Ad.objects.filter(category=category)[:200]
        if category != 999 and region != 999:
            queryset = models.Ad.objects.filter(region=region,category=category)[:200]
        return queryset

class SearchAd(generics.ListCreateAPIView):
    serializer_class = AdReadSerializer
    pagination_class = PaginationAds

    def get_queryset(self):
        category = self.kwargs['category']
        search_text = self.kwargs['search_text']
        region = self.kwargs['region']
        if category == 999 and region == 999:
            queryset = models.Ad.objects.filter(title__icontains=search_text)
        if category == 999 and region != 999:
            queryset = models.Ad.objects.filter(title__icontains=search_text,region=region)
        if category != 999 and region == 999:
            queryset = models.Ad.objects.filter(title__icontains=search_text,category=category)
        if category != 999 and region != 999:
            queryset = models.Ad.objects.filter(title__icontains=search_text,region=region,category=category)
        return queryset

'''class RegionAd(generics.ListAPIView):
    serializer_class = AdReadSerializer

    def get_queryset(self):
        reg_id=self.kwargs['id']
        return models.Ad.objects.filter(region=reg_id)'''

class Regions(generics.ListAPIView):
    serializer_class = RegionSerializer
    queryset = models.Region.objects.all()
    pagination_class = None

class Categories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = models.Category.objects.all()
    pagination_class = None

class Valutes(generics.ListAPIView):
    serializer_class = ValuteSerializer
    queryset = models.Valute.objects.all()
    pagination_class = None

class Stories(generics.ListAPIView):
    serializer_class = StorySerializer
    queryset = models.Story.objects.all().order_by('-pk')[:20]
    pagination_class = None


class Stories_Category(generics.ListAPIView):
    serializer_class = StorySerializer
    pagination_class = None

    def get_queryset(self):
        cat_id=self.kwargs['cat_id']
        return models.Story.objects.filter(story_category=cat_id).order_by('-pk')[:15]

class Story_View(generics.ListAPIView):
    serializer_class = StorySerializer
    pagination_class = None

    def get_queryset(self):
        _id=self.kwargs['id']
        return models.Story.objects.filter(pk=_id)

'''
class CarCreateUpdateView(generics.ListCreateAPIView):
    serializer_class = Car_Serializer
    http_method_names = ['post','delete','get','put']
    queryset = models.Car.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)
        images = request.FILES.getlist('car_media')
        car_id=models.Car.objects.create(title=request.data['title'])
        for image in images:
            #print(str(image)+' strrrrrr')
            models.Car_Media.objects.create(car=car_id,image=image)
        return Response(data=car_id.title)

class UserSerializer(serializers.ModelSerializer):
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

