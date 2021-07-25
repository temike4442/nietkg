from rest_framework import serializers
from doska import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields=('image',)

class ValuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Valute
        fields=('title',)

class AdSerializer(serializers.ModelSerializer):
    images_set=ImageSerializer(source='images',many=True,read_only=True)
    #valute=serializers.CharField(source='valute.title')
    valute=ValuteSerializer()
    #valute_name=serializers.CharField(source='valute.title')

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