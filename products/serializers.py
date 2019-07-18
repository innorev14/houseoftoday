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


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # queryset test 예정.
    # queryset = product.product_thumnail.all()
    # thumnail_images = ThumnailImageSerializer(queryset[0], many=True)
    thumnail_images = ThumnailImageSerializer(source='product_thumnail', many=True)

    class Meta:
        model = Product
        fields = ('id','name','price', 'thumnail_images')


# Product Detail에 관한 정보
class ProductDetailSerializer(serializers.ModelSerializer):
    thumnail_images = ThumnailImageSerializer(source='product_thumnail', many=True)
    detail_images = DetailImageSerializer(source='product_detail_images', many=True)
    product_option = ProductOptionSerializer(source='product_options', many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # products = ProductSerializer(source='category', many=True)

    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='category', many=True)

    class Meta:
        model = Category
        fields = '__all__'



