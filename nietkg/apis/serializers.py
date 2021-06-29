from rest_framework import serializers
from doska import models


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Images
        fields=('image',)

class AdSerializer(serializers.ModelSerializer):
    images_set=ImageSerializer(source='images',many=True,read_only=True)

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
            'images_set',
        ]