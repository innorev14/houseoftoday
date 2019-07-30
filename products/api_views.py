from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from datetime import date

import random


# import boto3
# from django.conf import settings
# from config import s3media


class CategoryListView(generics.ListAPIView):
    """
        스토어/카테고리 리스트를 불러옵니다.

        ---
        # 내용
            - id : 카테고리의 고유 ID
            - name : 카테고리 이름
            - image : 카테고리 이미지(URL Address)
    """
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryDetailView(generics.RetrieveAPIView):
    """
        스토어/카테고리 리스트에서 특정 id를 가지는 데이터를 불러옵니다.

        ---
        # 내용
            - id : 카테고리의 고유 ID

            - products : 카테고리에 속한 상품
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - price : 상품 가격
                - review_count : 리뷰 수
                - star_avg : 리뷰 평점
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                    - product : 썸네일 이미지가 속한 상품의 고유 ID
            - name : 카테고리 이름
            - image : 카테고리 이미지(URL Address)
    """
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = (AllowAny,)


class ProductListView(generics.ListAPIView):
    """
        상품 리스트를 불러옵니다.

        ---
        # 내용
            - id : 상품의 고유 ID
            - brand_name : 상품의 브랜드 이름
            - name : 상품 이름
            - price : 상품 가격
            - review_count : 리뷰 수
            - star_avg : 리뷰 평점
            - thumnail_images : 상품 썸네일 이미지
                - id : 썸네일 이미지의 고유 ID
                - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID
    """
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class ProductDetailView(generics.RetrieveAPIView):
    """
        상품 리스트에서 특정 id를 가지는 데이터를 불러옵니다.

        ---
        # 내용
            - id : 상품의 고유 ID

            - thumnail_images : 상품 썸네일 이미지
                - id : 썸네일 이미지의 고유 ID
                - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - detail_images : 상품 정보 이미지
                - id : 정보 이미지의 고유 ID
                - image : 정보 이미지(URL Address)
                - product : 정보 이미지가 속한 상품의 고유 ID

            - product_option : 상품 옵션
                - id : 옵션의 고유 ID
                - type : 옵션 타입
                - name : 옵션 이름
                - price : 옵션 가격
                - product : 옵션이 속한 상품의 고유 ID

            - review : 상품 리뷰
                - id : 리뷰의 고유 ID
                - star_score : 리뷰 별점
                - image : 리뷰 이미지
                - comment : 리뷰 내용
                - created : 리뷰 생성 일자
                - user : 리뷰 작성자
                - product : 리뷰가 속한 상품의 고유 ID
                - helpful : 리뷰 '도움이 돼요' - 아직 구현되지 않음

            - pdqna : 상품 QnA
                - id : QnA의 고유 ID
                - type : 질문 타입
                - comment : 질문 내용
                - completed : 답변 체크(미답변 = False, 답변완료 = True)
                - created : 질문 생성 일자
                - a_author : 답변 작성자
                - a_comment : 답변 내용
                - a_created : 답변 생성 일자
                - user : 질문 작성자
                - product : QnA가 속한 상품의 고유 ID

            < 상품 정보 데이터 >
            - name : 상품 이름
            - price : 상품 가격
            - brand_name : 상품 브랜드 이름
            - detail_name : 품명 및 모델명
            - detail_color : 색상
            - detail_size : 크기
            - detail_component : 구성품
            - detail_auth : KC인증 필 유무
            - detail_cost : 배송 설치비용
            - detail_standard : 품질보증기준
            - detail_mfc : 제조자
            - detail_mis : 제조국(수입여부)
            - detail_as : A/S책임자와 전화번호

            < 교환 및 환불 정보 데이터 >
            - return_fee : 반품/배송비
            - exchange_fee : 교환/배송비
            - return_address : 보내실 곳

            < 배송 관련 안내 정보 데이터 >
            - deliver : 배송
            - deliver_fee : 배송비
            - deliver_no_go : 배송불가 지역
            - deliver_fee_diff : 지역별 차등 배송비

            - created : 상품 업로드 생성 일자
            - discount_rate : 할인율
            - star_avg : 리뷰 평점
            - review_count : 리뷰 수
            - category : 상품이 속한 카테고리의 고유 ID

    """
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)


class ThumnailListView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ProductThumnail.objects.all()
    serializer_class = ThumnailImageSerializer
    permission_classes = (AllowAny,)


class ThumnailDetailView(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ProductThumnail.objects.all()
    serializer_class = ThumnailImageSerializer
    permission_classes = (AllowAny,)


class DetailImageListView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ProductDetailImage.objects.all()
    serializer_class = DetailImageSerializer
    permission_classes = (AllowAny,)


class DetailImageDetailView(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ProductDetailImage.objects.all()
    serializer_class = DetailImageSerializer
    permission_classes = (AllowAny,)


class ProductOptionListView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = (AllowAny,)


class ProductOptionDetailView(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
    permission_classes = (AllowAny,)


# google 검색어 : how to DRF serializer combine
# 참조 : https://stackoverflow.com/questions/45414928/combining-two-different-serializers-into-one-view-returning-named-json-arrays
class StoreHomeView(generics.ListAPIView):
    """
        스토어 홈 관련 정보를 모두 불러옵니다.

        ---
        # 내용
            - todaydeal : 오늘의 딜
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - review_count : 리뷰 수
                - star_avg : 리뷰 평점
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - categories: 카테고리
                - id : 카테고리의 고유 ID
                - name : 카테고리 이름
                - image : 카테고리 이미지(URL Address)

            - poular_products : 인기 상품
                - id : 상품의 고유 ID
                    - brand_name : 상품의 브랜드 이름
                    - name : 상품 이름
                    - discount_rate : 할인율
                    - price : 상품 가격
                    - thumnail_images : 상품 썸네일 이미지
                        - id : 썸네일 이미지의 고유 ID
                        - image : 썸네일 이미지(URL Address)
                    - product : 썸네일 이미지가 속한 상품의 고유 ID
    """
    renderer_classes = [JSONRenderer]
    serializer_class_product = ProductSerializer
    serializer_class_category = CategorySerializer

    permission_classes = (AllowAny,)

    # 하루가 지나면 오늘의 상품 날짜를 바꾸도록 HotDealNumber의 숫자 변경
    def updated_hot_deal_num(self):
        for i in range(1, 5):
            num = random.randrange(0, 181)
            print(num)
            HotDealNumber(id=i, product_rnd_number=num).save()

    def get_queryset_product(self):
        today = date.today()
        hot_deal_num = HotDealNumber.objects.all()

        if not today == hot_deal_num[0].updated:
            self.updated_hot_deal_num()

        result = Product.objects.all().filter(Q(id=hot_deal_num[0].product_rnd_number)
                                              | Q(id=hot_deal_num[1].product_rnd_number)
                                              | Q(id=hot_deal_num[2].product_rnd_number)
                                              | Q(id=hot_deal_num[3].product_rnd_number))
        return result

        # return Product.objects.all()

    def get_queryset_category(self):
        return Category.objects.all()

    def get_queryset_popularproducts(self):
        return Product.objects.all().order_by('-star_avg')

    def list(self, request, *args, **kwargs):
        todaydeal = self.serializer_class_product(self.get_queryset_product(), many=True)
        categories = self.serializer_class_category(self.get_queryset_category(), many=True)
        popular_products = self.serializer_class_product(self.get_queryset_popularproducts(), many=True)

        return Response({
            'todaydeal': todaydeal.data,
            'categories': categories.data,
            'popular_products': popular_products.data
        })


class RankingView(generics.ListAPIView):
    """
        랭킹 관련 정보를 모두 불러옵니다.

        ---
        # 내용
            - best100 : 카테고리별 BEST 100 정보(상품 100개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - review_count : 리뷰 수
                - star_avg : 리뷰 평점
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - light_homedeco : 조명&홈데코 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - daily_supplies : 생활용품 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - fabric : 패브릭 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - kitchenware : 주방용품 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - home_appliances : 가전제품 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - companion_animal : 반려동물 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID

            - furniture : 가구 BEST 정보(상품 10개)
                - id : 상품의 고유 ID
                - brand_name : 상품의 브랜드 이름
                - name : 상품 이름
                - discount_rate : 할인율
                - price : 상품 가격
                - thumnail_images : 상품 썸네일 이미지
                    - id : 썸네일 이미지의 고유 ID
                    - image : 썸네일 이미지(URL Address)
                - product : 썸네일 이미지가 속한 상품의 고유 ID
    """
    renderer_classes = [JSONRenderer]

    serializer_class_product = ProductSerializer
    # 각 Category별 제품을 분리시켜 받아오기 위해 사용.
    serializer_class_category_in_product = ProductSerializer
    # serializer_class_category_in_product = ProductSerializer(source='category', many=True)

    permission_classes = (AllowAny,)

    # 카테고리별 best100
    def get_queryset_product(self):
        return Product.objects.all().order_by('-star_avg')[0:100]

    # 조명&홈데코(category 명칭: 홈데코&조명)
    def get_queryset_category_in_product4(self):
        return Product.objects.filter(category__id='4').order_by('-star_avg')[0:10]

    # 생활용품(category 명칭: 수납/생활)
    def get_queryset_category_in_product6(self):
        return Product.objects.filter(category__id='6').order_by('-star_avg')[0:10]

    # 패브릭
    def get_queryset_category_in_product3(self):
        return Product.objects.filter(category__id='3').order_by('-star_avg')[0:10]

    # 주방용품(category 명칭: 주방)
    def get_queryset_category_in_product7(self):
        return Product.objects.filter(category__id='7').order_by('-star_avg')[0:10]

    # 가전제품
    def get_queryset_category_in_product5(self):
        return Product.objects.filter(category__id='5').order_by('-star_avg')[0:10]

    # 반려동물
    def get_queryset_category_in_product10(self):
        return Product.objects.filter(category__id='10').order_by('-star_avg')[0:10]

    # 가구
    def get_queryset_category_in_product2(self):
        return Product.objects.filter(category__id='2').order_by('-star_avg')[0:10]

    def list(self, request, *args, **kwargs):
        best100 = self.serializer_class_product(self.get_queryset_product(), many=True)
        light_homedeco = self.serializer_class_category_in_product(self.get_queryset_category_in_product4(), many=True)
        daily_supplies = self.serializer_class_category_in_product(self.get_queryset_category_in_product6(), many=True)
        fabric = self.serializer_class_category_in_product(self.get_queryset_category_in_product3(), many=True)
        kitchenware = self.serializer_class_category_in_product(self.get_queryset_category_in_product7(), many=True)
        home_appliances = self.serializer_class_category_in_product(self.get_queryset_category_in_product5(), many=True)
        companion_animal = self.serializer_class_category_in_product(self.get_queryset_category_in_product10(),
                                                                     many=True)
        furniture = self.serializer_class_category_in_product(self.get_queryset_category_in_product2(), many=True)

        return Response({
            'best100': best100.data,
            'light_homedeco': light_homedeco.data,
            'daily_supplies': daily_supplies.data,
            'fabric': fabric.data,
            'kitchenware': kitchenware.data,
            'home_appliances': home_appliances.data,
            'companion_animal': companion_animal.data,
            'furniture': furniture.data,
        })
        # 카테고리별 best100 : 'best100'
        # 조명&홈데코 4 : 'light_homedeco'
        # 생활용품 6 : 'daily_supplies'
        # 패브릭 3 : 'fabric'
        # 주방용품 7 : 'kitchenware'


        # 가전제품 5 : 'home_appliances'
        # 반려 동물 10 : 'companion_animal'
        # 가구 2 : 'furniture'

        # products = ProductSerializer(source='category', many=True)


class ReviewCreateAPIView(generics.CreateAPIView):
    """
        상품 리뷰를 생성합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있으며, 생성된 값이 리턴됩니다.
        image의 경우, 파일을 업로드해야 하기 때문에 json으로 요청하실 수 없고 Postman을 사용해야 합니다.

        # 내용
            - product : "리뷰가 속한 상품의 고유 ID"
            - star_score : "상품에 대한 리뷰 점수"
            - image : "업로드 할 리뷰 이미지"
            - comment : "업로드 할 내용"
    """
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewUpdateAPIView(generics.UpdateAPIView):
    """
        상품 리뷰의 특정 id를 가지는 데이터를 수정합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있으며, 수정된 값이 리턴됩니다.
        요청은 PUT, FETCH로 나뉩니다.
        image의 경우, 파일을 업로드해야 하기 때문에 json으로 요청하실 수 없고 Postman을 사용해야 합니다.

        # 내용
            - star_score : "상품에 대한 리뷰 점수"
            - image : "업로드 할 리뷰 이미지"
            - comment : "업로드 할 내용"
    """
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer


class PDQnACreateAPIView(generics.CreateAPIView):
    """
        상품 문의를 생성합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있으며, 수정된 값이 리턴됩니다.

        # 내용
            - product : "문의가 속한 상품의 고유 ID"
            - type : "상품에 대한 문의유형"
            - comment : "문의 할 내용"
    """
    queryset = PDQnA.objects.all()
    serializer_class = PDQnACreateSerializer

    # ############ def perform_create(self, serializer): 사용시 주의사항 ############
    # serializer.save는 단 한번만 이뤄져야 함. 여러번 save를 하여 각 필드마다 넣을 수 있으나,
    # 그럴 경우 receiver에서 여러번 실행될 수 있기 때문에 save할때 한번에 여러 필드를 저장하는게 맞다.
    # 왠만한 stackoverflow 답변 글에서도 serializer.save() 는 한번만 사용하도록 답변이 달림.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PDQnADeleteAPIView(generics.DestroyAPIView):
    """
        상품 문의의 특정 id를 가지는 데이터를 삭제합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        상품 문의의 고유 ID를 입력하면 삭제됩니다.
    """
    queryset = PDQnA.objects.all()


class ProductOrderCartCreateAPIView(generics.CreateAPIView):
    """
        로그인 중인 회원의 상품 장바구니를 생성합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있으며, 생성된 값이 리턴됩니다.

        # 내용
            - product_option : "상품에 속한 상품옵션의 고유 ID"
    """
    renderer_classes = [JSONRenderer]

    queryset = ProductOrderCart.objects.all()
    serializer_class = ProductOrderCartCreateSerializer
    # AllowAny를 변경해야함. 회원만 주문 가능하도록.. 임시방편.
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductOrderCartAPIView(generics.ListAPIView):
    """
        로그인 중인 회원의 상품 장바구니 정보를 불러옵니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        # 내용
            - id : 상품 장바구니 고유 ID
            - brand_name : 상품의 브랜드 이름
            - product : 상품 이름
            - deliver : 배송
            - deliver_fee : 배송비
            - product_option : 상품 옵션
            - price : 상품 가격
            - user : 로그인한 유저의 고유 ID
            - image : 해당 상품에 대한 대표 썸네일 이미지(1장) url
    """
    renderer_classes = [JSONRenderer]

    queryset = ProductOrderCart.objects.all()
    serializer_class = ProductOrderCartSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user.id)
        return queryset


class PaymentCreateAPIView(generics.CreateAPIView):
    """
        로그인 중인 회원 상품 장바구니 안의 상품을 결제합니다. 결제 후 결제 완료된 장바구니 안의 상품이 삭제되며, 주문상품목록에 결제된 상품이 등록됩니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        토큰 인증을 하신 후, 내용없이 요청하시면 됩니다.
    """
    renderer_classes = [JSONRenderer]

    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer

    # # AllowAny를 변경해야함. 회원만 주문 가능하도록.. 임시방편.
    # permission_classes = (AllowAny,)

    # ############ def perform_create(self, serializer): 사용시 주의사항 ############
    # serializer.save는 단 한번만 이뤄져야 함. 여러번 save를 하여 각 필드마다 넣을 수 있으나,
    # 그럴 경우 receiver에서 여러번 실행될 수 있기 때문에 save할때 한번에 여러 필드를 저장하는게 맞다.
    # 왠만한 stackoverflow 답변 글에서도 serializer.save() 는 한번만 사용하도록 답변이 달림.
    def perform_create(self, serializer):
        user = self.request.user
        total_price = user.cart.aggregate(Sum('product_option_id__price'))['product_option_id__price__sum']
        serializer.save(user=user, product_price=total_price, deliver_price=0, total_price=total_price)


class DirectPaymentCreateAPIView(generics.CreateAPIView):
    """
        로그인 중인 회원이 구매하고자 하는 상품을 바로(직접)결제합니다. 결제 후 주문상품목록에 결제된 상품이 등록됩니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        토큰 인증을 하신 후 다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - product_option : "상품에 속한 상품옵션의 고유 ID"

        다음과 같이 리턴됩니다.

        # 내용
            - id : 직접결제하기의 고유 ID
            - product_price : 선택한 상품옵션의 가격
            - deliver_price : 배송비
            - total_price : 최종 합산 가격
            - created : 생성일자
            - product_option : 선택한 상품옵션의 고유 ID
    """
    renderer_classes = [JSONRenderer]

    queryset = DirectPayment.objects.all()
    serializer_class = DirectPaymentCreateSerializer

    # ############ def perform_create(self, serializer): 사용시 주의사항 ############
    # serializer.save는 단 한번만 이뤄져야 함. 여러번 save를 하여 각 필드마다 넣을 수 있으나,
    # 그럴 경우 receiver에서 여러번 실행될 수 있기 때문에 save할때 한번에 여러 필드를 저장하는게 맞다.
    # 왠만한 stackoverflow 답변 글에서도 serializer.save() 는 한번만 사용하도록 답변이 달림.
    def perform_create(self, serializer):
        user = self.request.user
        product_option_id = self.request.POST['product_option']
        price = ProductOption.objects.get(pk=int(product_option_id)).price

        serializer.save(user=user, product_price=price, deliver_price=0, total_price=price)


class PaymentAPIView(generics.ListAPIView):
    """
        로그인 중인 사용자의 결제 완료된 목록을 보여줍니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        # 내용
            - id : 결제 고유 ID, 주문 번호로 활용 가능
            - order_products : 주문한 상품 목록
                - product : 주문한 상품 이름
                - product_option : 주문한 상품 옵션
            - product_price : 주문한 상품의 전체 가격
            - deliver_price : 배송비
            - total_price : 총 결제 가격
            - created : "결제 완료 일자"
    """
    renderer_classes = [JSONRenderer]

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user.id)
        return queryset


# review 작성 시 상품의 전체 리뷰 수와 평점이 계산됨
@receiver(post_save, sender=Review)
def calculate_review(sender, **kwargs):
    pd = kwargs['instance'].product
    pd.review_count = pd.reviews.count()
    pd.star_avg = pd.reviews.aggregate(Avg('star_score'))['star_score__avg']
    pd.save()


# 결제 완료 시(Payment model save) 장바구니 모델에 저장되있던 목록을 주문 목록으로 옮기고 장바구니 모델 저장 내용 삭제
@receiver(post_save, sender=Payment)
def after_payment(sender, **kwargs):
    cart_delete_list = []
    pm = kwargs['instance'].id
    user = kwargs['instance'].user
    pd_in_cart_num = user.cart.count()
    for pd in range(0, pd_in_cart_num):
        # print(user.cart.all()[pd].product_option.id)
        OrderProduct(user_id=user.id, product_option_id=user.cart.all()[pd].product_option.id, payment_id=pm).save()
        cart_item = ProductOrderCart.objects.all().get(Q(user_id=user.id) & Q(id=user.cart.all()[pd].id))
        cart_delete_list.append(cart_item.id)

    for idx in cart_delete_list:
        cart_delete_item = ProductOrderCart.objects.get(pk=idx)
        cart_delete_item.delete()


# DirectPayment(직접결제)를 실행하게 될 경우 실행.
@receiver(post_save, sender=DirectPayment)
def after_direct_payment(sender, **kwargs):
    # DirectPayment의 번호.
    pm = kwargs['instance'].id
    # 현재 로그인한 해당 유저의 번호.
    user = kwargs['instance'].user
    # 현재 선택한 상품옵션의 번호.
    po_id = kwargs['instance'].product_option_id
    # OrderProduct(직접결제하기) 테이블에 레코드를 저장함. ()에 저장할 필드를 적고, 단 한번만 save 시키면 됨.
    OrderProduct(user_id=user.id, product_option_id=po_id, direct_payment_id=pm).save()



# 리뷰를 삭제할 경우 AWS S3에도 삭제되도록 함
# @receiver(post_delete, sender=Review)
# def post_delete(sender, instance, **kwargs):
#     session = boto3.Session(
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#         region_name=s3media.MediaStorage.region_name
#     )
#
#     # s3.Objects는 s3에 업로드된 파일 객체를 얻어오는 클래스
#     # arg1 = 버킷네임
#     # arg2 = 파일 경로 - Key
#     s3 = session.resource('s3') # s3 권한 가져오기
#     image = s3.Object(s3media.MediaStorage.bucket_name, str(instance.image))
#     image.delete()
