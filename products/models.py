from django.db import models

from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    # 카테고리 이름
    name = models.CharField(max_length=45)
    # 카테고리 이미지
    image = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Product(models.Model):
    # 상품 이름
    name = models.CharField(max_length=45)
    # 상품 가격
    price = models.PositiveIntegerField(default=0)
    # 상품을 제공한 브랜드 이름
    brand_name = models.CharField(max_length=45)
    # 상품이 속한 카테고리
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category', null=True)
    # 상품 상세정보 - 품명 및 모델명
    detail_name = models.CharField(max_length=100)
    # 상품 상세정보 - 색상
    detail_color = models.CharField(max_length=30)
    # 상품 상세정보 - 크기
    detail_size = models.CharField(max_length=200)
    # 상품 상세정보 - 구성품
    detail_component = models.TextField()
    # 상품 상세정보 - KC인증 필 유무
    detail_auth = models.TextField()
    # 상품 상세정보 - 배송 유무
    detail_cost = models.TextField()
    # 상품 상세정보 - 품질보증기준
    detail_standard = models.TextField()
    # 상품 상세정보 - 제조자
    detail_mfc = models.CharField(max_length=200)
    # 상품 상세정보 - 제조국
    detail_mis = models.CharField(max_length=45)
    # 상품 상세정보 - A/S 책임자 및 전화번호
    detail_as = models.CharField(max_length=100)
    # 교환 및 환불 - 반품/배송비
    return_fee = models.CharField(max_length=100)
    # 교환 및 환불 - 교환/배송비
    exchange_fee = models.CharField(max_length=100)
    # 교환 및 환불 - 반품 주소
    return_address = models.TextField()
    # 배송 관련 안내 - 배송
    deliver = models.CharField(max_length=100, default='일반택배배송')
    # 배송 관련 안내 - 배송비
    deliver_fee = models.CharField(max_length=100, default='무료배송')
    # 배송 관련 안내 - 배송불가 지역
    deliver_no_go = models.CharField(max_length=100, default='배송불가 지역이 없습니다.')
    # 배송 관련 안내 - 지역별 차등배송비
    deliver_fee_diff = models.CharField(max_length=100, default='없음')
    # 생성일자
    created = models.DateField(auto_now_add=True)
    # 할인율
    discount_rate = models.CharField(max_length=3, blank=True, null=True)
    # 상품에 대한 리뷰 평균 평점
    star_avg = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    # 상품에 대한 리뷰 개수
    review_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        # 객체의 이름 - 상품 이름
        return self.name

    class Meta:
        ordering = ['id']


class ProductThumnail(models.Model):
    # 상품 썸네일 이미지 - url 주소로 저장
    image = models.TextField()
    # 썸네일 이미지가 속한 상품
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_thumnail')

    def __str__(self):
        # 객체의 이름 - 썸네일 이미지의 url 주소
        return self.image

    class Meta:
        ordering = ['id']


class ProductDetailImage(models.Model):
    # 상품 정보에서 보이는 이미지 - url 주소로 저장
    image = models.TextField()
    # 상품 정보 이미지가 속한 상품
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_detail_images')

    def __str__(self):
        # 객체의 이름 - 상품 정보 이미지의 url 주소
        return self.image

    class Meta:
        ordering = ['id']


class ProductOption(models.Model):
    # 상품 옵션의 타입 ex) 색상, 크기 등등
    type = models.CharField(max_length=45)
    # 옵션 선택 - 옵션 이름 + 가격
    name = models.CharField(max_length=100)
    # 옵션 가격
    price = models.PositiveIntegerField()
    # 옵션이 속한 상품
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_options')

    def __str__(self):
        # 객체의 이름 - 상품 옵션의 이름
        return self.name

    class Meta:
        ordering = ['id']


class Review(models.Model):
    # 작성자
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    # 리뷰가 속한 상품
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    # 별점
    star_score = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    # 리뷰 이미지 - url 주소 저장
    image = models.ImageField(upload_to='store/review/%Y/%m/%d', blank=True, null=True)
    # 리뷰 내용
    comment = models.TextField()
    # '도움이 돼요' 버튼에 대한 필드
    helpful = models.ManyToManyField(User, related_name='helpful_reviews', blank=True, null=True)
    # 생성 일자
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        # 객체의 이름 - 질문 작성자
        return self.user.username

    class Meta:
        ordering = ['id']


class PDQnA(models.Model):
    # 질문 유형
    type = models.CharField(max_length=30)
    # 질문 내용
    comment = models.TextField()
    # 답변 체크
    completed = models.BooleanField(default=False)
    # 작성자 생성 일자
    created = models.DateField(auto_now_add=True)
    # 작성자
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    # 질문이 속한 상품
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='question')

    # 답변 작성자
    a_author = models.CharField(max_length=20)
    # 답변 내용
    a_comment = models.TextField(blank=True, null=True)
    # 답변 생성 일자
    a_created = models.DateField(auto_now=True)

    def __str__(self):
        # 객체의 이름 - 리뷰 작성자
        return self.user.username

    class Meta:
        ordering = ['id']


class HotDealNumber(models.Model):
    # 랜덤 숫자를 위한 필드
    product_rnd_number = models.PositiveIntegerField(default=0)
    # 날짜 비교를 위한 필드
    updated = models.DateField(auto_now=True)

    def __str__(self):
        # 객체의 이름 - 랜덤 숫자
        return str(self.product_rnd_number)

    class Meta:
        ordering = ['id']


# 장바구니
class ProductOrderCart(models.Model):
    # 주문하는 유저
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    # 상품 옵션
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return "(" + self.user.username + ")" + self.product_option.name

    class Meta:
        ordering = ['id']

    # def save(self, *args, **kwargs):
    #     if self.product_option.product != self.product:
    #         raise ValueError('ProductOrderItem의 product_option은 선택된 product의 옵션이어야 합니다')
    #     super().save(*args, **kwargs)


# 결제
class Payment(models.Model):
    # 결제하는 유저
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    # 총 상품 금액
    product_price = models.PositiveIntegerField(default=0)
    # 배송비
    deliver_price = models.PositiveIntegerField(default=0)
    # 총결제금액, Total payment amount,
    total_price = models.PositiveIntegerField(default=0)
    # 생성날짜 및 시간
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "(" + self.user.username + ")" + "주문번호:" + str(self.id)

    class Meta:
        ordering = ['id']


# 결제 후 이동한 상품목록 = 주문이 완료된 상품 목록
class OrderProduct(models.Model):
    # 주문한 유저
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_product')
    # 주문한 상품 옵션
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE, related_name='order_product')
    # 주문한 결제 번호
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='order_product')
    # 생성 일자
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "(" + self.user.username + ")" + self.product_option.name

    class Meta:
        ordering = ['id']
