from rest_framework import serializers
from .models import *


class ThumnailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_thumnail
        fields = '__all__'


class DetailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_detail_images
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    thumnail_images = ThumnailImageSerializer(source='product_thumnail', many=True)
    detail_images = DetailImageSerializer(source='product_detail_images', many=True)

    class Meta:
        model = Products
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='category', many=True)

    class Meta:
        model = Categorys
        fields = '__all__'

# 카테고리 불렀을때 프로덕트도 다 가져오도록 시리얼라이저 만들어야함..

# 프로덕트, 썸네일, 이미지 관련 시리얼라이저 전제 목록 나오도록 만들기.

# Cartegory

# Product / thumnail / detail_images => Queryset을 이용해서 , related_name을 이용해서 구현하기.
#   --> ListView, DetailView 만들기..

# Product / thumnail / detail_images 만들면 Category에 전체 뿌려지도록 Queryset 써야한다..
