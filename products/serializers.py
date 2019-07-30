from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *

# 썸네일 이미지 정보 전체 보여주기용
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
# source 관련 참조 : https://stackoverflow.com/questions/32166826/django-rest-framework-how-to-get-field-of-foreign-key-of-a-foreign-key
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

    def to_representation(self, instance):
        serializer_data = super().to_representation(instance)
        # instance: 구매자, 상품옵션번호, 상품옵션이름 이 나옴. ex) (admin)06. 모노릴렉스(누빔)(15,900원)
        # print(instance)
        # serializer_data['product']: 상품옵션이름이 나옴. --> ex) 디어썸머 리플 여름차렵이불(단품/세트) 14colors
        # print(serializer_data['product'])
        pd = Product.objects.get(name=serializer_data['product'])
        # Product와 현재Cart내 상품에 맞는게 나오도록 filter를 걸어줌. print결과로는 안보이나 그렇다.. ex) 디어썸머 리플 여름차렵이불(단품/세트) 14colors
        # print(pd)
        # QuerySet으로 ProductThumnail에 관한 여러 필드의 값을 Dictionary형태로 받아온다.
        # print(pd.product_thumnail.all())
        # Queryset의 여러 값 중 최상단(각 상품의 최상단 id 한개) 하나를 가져옴.
        thumnail_images = pd.product_thumnail.all()[0]
        # 여러 필드의 값 중 image에 해당하는 url Text만 별개로 가져온다.
        serializer_data['image'] = thumnail_images.image
        # 해당 url을 리턴시킴. 여기서 변수명은 'image' 로써, 출력값은 ex) "image": "https://image.ohou.se/image/..." 으로 나오게 된다.
        return serializer_data


# 주문이 완료된 상품 목록
class OrderProductSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product_option.product.name')
    product_option = serializers.CharField(source='product_option.name')

    class Meta:
        model = OrderProduct
        fields = ['product', 'product_option']


# POST - 결제하기(장바구니 이용)
class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ['user']


# POST - 바로결제하기(장바구니 없이 직접)
class DirectPaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectPayment
        exclude = ['user']


# GET - 결제한 목록 보기
class PaymentSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(source='order_product', many=True)

    class Meta:
        model = Payment
        exclude = ['user']
