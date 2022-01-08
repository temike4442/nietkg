from rest_framework import serializers
from doska import models

class StoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StoryItem
        fields = ('story_type','story_src')

class StorySerializer(serializers.ModelSerializer):
    items_set = StoryItemSerializer(source='story_items',many=True,read_only=True)
    class Meta:
        model = models.Story
        fields = [
            'story_title',
            'story_category',
            'items_set'
        ]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields=('image','ad')

class AdReadSerializer(serializers.ModelSerializer):
    images_set=ImageSerializer(source='images',many=True,read_only=True)
    valute=serializers.ReadOnlyField(source='valute.title')
    category=serializers.ReadOnlyField(source='category.title')
    region=serializers.ReadOnlyField(source='region.title')

    class Meta:
        model=models.Ad
        fields=[
            'pk',
            'title',
            'content',
            'category',
            'number',
            'name',
            'region',
            'address',
            'price',
            'valute',
            'date',
            'images_set',
        ]
class AdWriteSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,required=False)
    class Meta:
        model = models.Ad
        fields=[
            'title',
            'content',
            'category',
            'number',
            'name',
            'region',
            'address',
            'price',
            'valute',
            'images'
        ]

class ValuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Valute
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields = '__all__'
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Region
        fields = '__all__'

'''
class Car_Media_Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.Car_Media
        fields = ('car','image',)

class Car_Serializer(serializers.ModelSerializer):
    car_media = Car_Media_Serializer(many=True,required=False)
    class Meta:
        model = models.Car
        fields = ('title','car_media')


    def create(self, validated_data):
     #   #if 'car_media' in validated_data:
        title = validated_data.get('title')
        car_media = validated_data.get('car_media')
        car_instance= models.Car.objects.create(title=title)
        models.Car_Media.objects.create(car=car_instance,image=car_media)
        ##for img in car_media:
            #models.Car_Media.objects.create(car=car_instance,image=img)
        return car_instance

        #if 'car_media' not in validated_data:
            #car_instance= models.Car.objects.create(**validated_data)
            #return car_instance'''
