from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['id', 'name', 'image']


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'brand_name', 'category', 'detail_name', 'detail_color', 'detail_size',
              'detail_component', 'detail_auth', 'detail_cost', 'detail_standard', 'detail_mfc', 'detail_mis',
              'detail_as', 'return_fee', 'exchange_fee', 'return_address', 'deliver', 'deliver_fee', 'deliver_no_go',
              'deliver_fee_diff', 'discount_rate', 'star_avg', 'review_count']
    list_display = ['id', 'name', 'price', 'brand_name', 'star_avg', 'review_count']


class ProductThumnailAdmin(admin.ModelAdmin):
    fields = ['image', 'product']
    list_display = ['id', 'image', 'product']


class ProductDetailImageAdmin(admin.ModelAdmin):
    fields = ['image', 'product']
    list_display = ['id', 'image', 'product']


class ProductOptionAdmin(admin.ModelAdmin):
    fields = ['type', 'name', 'price', 'product']
    list_display = ['id', 'type', 'name', 'price', 'product']


class ReviewAdmin(admin.ModelAdmin):
    fields = ['user', 'product', 'star_score', 'image', 'comment']
    list_display = ['id', 'user', 'product', 'star_score', 'image', 'comment', 'created']


class PDQnAAdmin(admin.ModelAdmin):
    fields = ['type', 'comment', 'completed', 'user', 'product', 'a_author', 'a_comment']
    list_display = ['id', 'type', 'comment', 'completed', 'created', 'user', 'product', 'a_author', 'a_comment',
                    'a_created']


class HotDealNumberAdmin(admin.ModelAdmin):
    fields = ['product_rnd_number']
    list_display = ['id', 'product_rnd_number', 'updated']


# 장바구니Admin
class ProductOrderCartAdmin(admin.ModelAdmin):
    fields = ['user', 'product_option']
    list_display = ['id', 'user', 'product_option']


# 결제(장바구니를 통한)Admin
class PaymentAdmin(admin.ModelAdmin):
    fields = ['user', 'product_price', 'deliver_price', 'total_price']
    list_display = ['id', 'user', 'product_price', 'deliver_price', 'total_price', 'created']


# 바로결제하기Admin
class DirectPaymentAdmin(admin.ModelAdmin):
    fields = ['user', 'product_option', 'product_price', 'deliver_price', 'total_price']
    list_display = ['id', 'product_option', 'user', 'product_price', 'deliver_price', 'total_price', 'created']


# 결제상품목록Admin
class OrderProductAdmin(admin.ModelAdmin):
    fields = ['user', 'product_option', 'payment', 'direct_payment']
    list_display = ['id', 'user', 'product_option', 'payment', 'direct_payment', 'created']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductThumnail, ProductThumnailAdmin)
admin.site.register(ProductDetailImage, ProductDetailImageAdmin)
admin.site.register(ProductOption, ProductOptionAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(PDQnA, PDQnAAdmin)
admin.site.register(HotDealNumber, HotDealNumberAdmin)
admin.site.register(ProductOrderCart, ProductOrderCartAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(DirectPayment, DirectPaymentAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
