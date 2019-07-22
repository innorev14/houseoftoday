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
        fields = ('star_score',)


class PDQnASerializer(serializers.ModelSerializer):
    class Meta:
        model = PDQnA
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    # 읽기 전용으로, serializer 클래스에서 메서드를 호출하여 값을 가져옴.
    thumnail_images = SerializerMethodField()
    # 상품 리뷰 별점에 관한 필드 추가.
    # review 대신 리뷰평점 계산을 한 start_score 넣음.
    review = ReviewScoreSerializer(source='reviews', many=True)
    # star_score = serializers.SerializerMethodField()

    class Meta:
        model = Product
        # fields = ('id', 'brand_name', 'name', 'price', 'thumnail_images', 'star_score',)
        fields = ('id', 'brand_name', 'name', 'price', 'thumnail_images', 'review')

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

    # def get_star_score(self, star_score):
    #     # 평균 = 모델리뷰 star_score 평균값(소수점 버림). 뒤에 get('star_score__avg') 은 star_score__avg 변수명을 star_score로 변경시켜준다.
    #
    #     # for i in range(0, 25):
    #     #     average(i) = Review.objects.filter(product__id=i).aggregate(Avg('star_score')).get('star_score__avg')
    #
    #     # total_points = Review.objects.aggregate(Sum('star_score'))['star_score__sum']
    #     # num_products = Review.objects.count()
    #     # average = total_points / num_products
    #     # average = Review.objects.all().annotate(num_products=Count('id')).aggregate(Avg('star_score'))
    #
    #     # sum_score = 0
    #     # for i in range(0,10):
    #     #     for j in range(0,10):
    #     #         sum_score += int(Review.objects.filter(product__id=i)[j].star_score)
    #     #
    #     # average = round(sum_score / 10,1)
    #
    #
    #     # average = Review.objects.values('product')
    #     # average = Review.objects.all().aggregate(Avg('star_score')).get('star_score__avg')
    #     # average = round(Review.objects.all().aggregate(Avg('star_score')).get('star_score__avg'), 2)
    #
    #     average = round(Review.objects.all().aggregate(Avg('star_score')).get('star_score__avg'), 2)
    #
    #     # if average is None:
    #     if average == None:
    #         return 0
    #     return average


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

