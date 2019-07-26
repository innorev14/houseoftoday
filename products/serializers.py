from django.db.models import Avg, Count, F, Sum, Case, When
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

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


# Category-Product에 뿌려줄 리뷰점수(star_score) field만 있으면 됨.
class ReviewScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['star_score']


class PDQnASerializer(serializers.ModelSerializer):
    class Meta:
        model = PDQnA
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # 읽기 전용으로, serializer 클래스에서 메서드를 호출하여 값을 가져옴.
    thumnail_images = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'brand_name', 'name', 'discount_rate', 'price', 'review_count', 'star_avg', 'thumnail_images']

    # 함수명은 get_[related_name field]로써,
    # def get_[related_name](self, [models.py에서 해당 class 내 related_name의 변수명]): 을 가져오면 됨.
    def get_thumnail_images(self, product):
        # filter는 object를 이용해 가져옴으로써, slice(잘라서)를 통해 원하는 내용을 가져올 수 있음.
        # Queryset처럼 일반적으로 해당 부분만 불러오도록 뒤에[0] 등을 사용하면 Err 발생함.
        thumnail_images = ProductThumnail.objects.filter(product=product)[0:1]
        # 인스턴스에 해당 내용을 넣어 실제 filtering을 실시함.
        serializer = ThumnailImageSerializer(instance=thumnail_images, many=True)
        # filtering된 내용의 data를 반환함.
        return serializer.data


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


# average = round(Review.objects.all().aggregate(Avg('star_score')).get('star_score__avg'), 2)
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'star_score', 'image', 'comment']


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['star_score', 'image', 'comment']


class PDQnACreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDQnA
        fields = ['product', 'type', 'comment']


# POST - 장바구니
class ProductOrderCartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrderCart
        fields = ['product_option']


# GET - 장바구니
class ProductOrderCartSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='product_option.product.brand_name')
    product = serializers.CharField(source='product_option.product.name')
    deliver = serializers.CharField(source='product_option.product.deliver')
    deliver_fee = serializers.CharField(source='product_option.product.deliver_fee')
    product_option = serializers.CharField(source='product_option.name')
    price = serializers.IntegerField(source='product_option.price')

    class Meta:
        model = ProductOrderCart
        fields = '__all__'


# 주문이 완료된 상품 목록
class OrderProductSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product_option.product.name')
    product_option = serializers.CharField(source='product_option.name')

    class Meta:
        model = OrderProduct
        fields = ['product', 'product_option']


# POST - 결제하기
class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ['user']


# GET - 결제한 목록 보기
class PaymentSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(source='order_product', many=True)

    class Meta:
        model = Payment
        exclude = ['user']
