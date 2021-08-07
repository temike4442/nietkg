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
        fields=('image',)

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
            'images_set',
        ]
class AdWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Ad
        fields = '__all__'

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

