from rest_framework import serializers
from .models import *


class ThumnailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductThumnail
        fields = '__all__'


class DetailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetailImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    thumnail_images = ThumnailImageSerializer(source='product_thumnail', many=True)
    detail_images = DetailImageSerializer(source='product_detail_images', many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='category', many=True)

    class Meta:
        model = Category
        fields = '__all__'
