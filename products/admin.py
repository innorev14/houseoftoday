from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['id', 'name', 'image']


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'brand_name', 'category', 'detail_name', 'detail_color', 'detail_size',
              'detail_component', 'detail_auth', 'detail_cost', 'detail_standard', 'detail_mfc', 'detail_mis',
              'detail_as', 'return_fee', 'exchange_fee', 'return_address', 'deliver', 'deliver_fee', 'deliver_no_go',
              'deliver_fee_diff']
    list_display = ['id', 'name', 'price', 'brand_name', 'category', 'detail_name', 'detail_color', 'detail_size',
                    'detail_component', 'detail_auth', 'detail_cost', 'detail_standard', 'detail_mfc', 'detail_mis',
                    'detail_as', 'return_fee', 'exchange_fee', 'return_address', 'deliver', 'deliver_fee',
                    'deliver_no_go', 'deliver_fee_diff', 'created']


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
    fields = ['user', 'product', 'score_durability', 'score_price', 'score_design', 'score_delivery', 'image',
              'comment', 'helpful']
    list_display = ['id', 'user', 'product', 'score_durability', 'score_price', 'score_design', 'score_delivery',
                    'image', 'comment', 'helpful', 'created']


class PDQnAAdmin(admin.ModelAdmin):
    fields = ['type', 'comment', 'completed', 'user', 'product', 'a_author', 'a_comment']
    list_display = ['id', 'type', 'comment', 'completed', 'created', 'user', 'product', 'a_author', 'a_comment',
                    'a_created']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductThumnail, ProductThumnailAdmin)
admin.site.register(ProductDetailImage, ProductDetailImageAdmin)
admin.site.register(ProductOption, ProductOptionAdmin)
admin.site.register(Review)
admin.site.register(PDQnA, PDQnAAdmin)
