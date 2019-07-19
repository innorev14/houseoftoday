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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class PDQnASerializer(serializers.ModelSerializer):
    class Meta:
        model = PDQnA
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # queryset test 예정.
    # queryset = product.product_thumnail.all()[-1:].data
    # thumnail_images = ThumnailImageSerializer(queryset, many=True)
    # thumnail_images = serializers.SerializerMethodField()

    thumnail_images = ThumnailImageSerializer(source='product_thumnail', many=True)

    # def get_thumnail_oneimage(self, product):
    #     queryset = product.product_thumnail.all()[-1:]
    #     return ThumnailImageSerializer(queryset, many=True).data

    class Meta:
        model = Product
        fields = ('id','name','price', 'thumnail_images')


# Product Detail에 관한 정보
class ProductDetailSerializer(serializers.ModelSerializer):
    thumnail_images = ThumnailImageSerializer(source='product_thumnail', many=True)
    detail_images = DetailImageSerializer(source='product_detail_images', many=True)
    product_option = ProductOptionSerializer(source='product_options', many=True)
    review = ReviewSerializer(source='reviews', many=True)
    pdqna = PDQnASerializer(source='question', many=True)


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



