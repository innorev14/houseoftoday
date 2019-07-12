from django.db import models

from accounts.models import User


class Categorys(models.Model):
    name = models.CharField(max_length=45)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=45)
    price = models.IntegerField()
    brand_name = models.CharField(max_length=45)
    category = models.ForeignKey(Categorys, on_delete=models.SET_NULL, related_name='category', null=True)
    detail_name = models.CharField(max_length=100) # 상품 상세정보 - 품명 및 모델명
    detail_color = models.CharField(max_length=30) # 상품 상세정보 - 색상
    detail_size = models.CharField(max_length=100) # 상품 상세정보 - 크기
    detail_component = models.CharField(max_length=45) # 상품 상세정보 - 구성품
    detail_auth = models.CharField(max_length=45) # 상품 상세정보 - KC인증 필 유무
    detail_cost = models.CharField(max_length=45) # 상품 상세정보 - 배송 유무
    detail_standard = models.CharField(max_length=100) # 상품 상세정보 - 품질보증기준
    detail_mfc = models.CharField(max_length=50) # 상품 상세정보 - 제조자
    detail_mis = models.CharField(max_length=45) # 상품 상세정보 - 제조국
    detail_as = models.CharField(max_length=100) # 상품 상세정보 - A/S 책임자 및 전화번호
    return_fee = models.CharField(max_length=100) # 교환 및 환불 - 반품/배송비
    exchange_fee = models.CharField(max_length=100) # 교환 및 환불 - 교환/배송비
    return_address = models.TextField() # 교환 및 환불 - 반품 주소
    deliver = models.CharField(max_length=100, default='업체직접배송') # 배송 관련 안내 - 배송
    deliver_fee = models.CharField(max_length=100, default='무료배송') # 배송 관련 안내 - 배송비
    deliver_no_go = models.CharField(max_length=100, default='배송불가지역이 없습니다.') # 배송 관련 안내 - 배송불가지역
    deliver_fee_diff = models.CharField(max_length=100, default='없음') # # 배송 관련 안내 - 지역별 차등배송비
    created = models.DateField(auto_now_add=True)  # 생성일자

    def __str__(self):
        return self.name

class Product_thumnail(models.Model):
    pd_image = models.ImageField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_thumnail')

    def __str__(self):
        return self.pd_image

class Product_detail_images(models.Model):
    pd_detail_image = models.ImageField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_detail_images')

    def __str__(self):
        return self.pd_detail_image

class Product_options(models.Model):
    type = models.CharField(max_length=45)  # 상품 구별 - 상품/색상 등 구별하는 것.
    option_name = models.CharField(max_length=100) # 옵션선택 - 전체이름 + 가격
    option_price = models.PositiveIntegerField() # 옵션선택 - 가격만 나오도록.
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_options')

    def __str__(self):
        return self.option_name



class reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    pd_durability = models.IntegerField() # 내구성
    pd_price = models.IntegerField()  # 가격
    pd_design = models.IntegerField()  # 디자인
    pd_delivery = models.IntegerField()  # 배송
    rv_image = models.ImageField() # 리뷰전용 이미지
    comment = models.TextField() # 내용
    # helpful_counts = models.IntegerField() # 도움이 돼요.
    helpful = models.ManyToManyField(User, related_name='helpful_reviews', blank=True)
    created = models.DateField(auto_now_add=True) # 생성일자


class PD_Question(models.Model):
    type = models.CharField(max_length=30) # 유형
    comment = models.TextField() # 답변내용
    completed = models.BooleanField(default=False) # 답변 체크
    created = models.DateField(auto_now_add=True) # 생성일자
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='question')


class PD_Answer(models.Model):
    comment = models.TextField() # 답변내용
    created = models.DateField(auto_now_add=True)  # 생성일자
    question = models.ForeignKey(PD_Question, on_delete=models.CASCADE, related_name='answer')


