from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

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
                - name : 상품 이름
                - price : 상품 가격
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
            - name : 상품 이름
            - price : 상품 가격
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
