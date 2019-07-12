from django.contrib import admin
from .models import *

class CategorysAdmin(admin.ModelAdmin):
    fields = ['name','image']
    list_display = ('id','name','image',)

class ProductsAdmin(admin.ModelAdmin):
    fields = ['name','price','brand_name','category','detail_name','detail_color','detail_size','detail_component','detail_auth','detail_cost','detail_standard','detail_mfc','detail_mis','detail_as','return_fee','exchange_fee','return_address','deliver','deliver_fee','deliver_no_go','deliver_fee_diff']
    list_display = ('id','name','price','brand_name','category','detail_name','detail_color','detail_size','detail_component','detail_auth','detail_cost','detail_standard','detail_mfc','detail_mis','detail_as','return_fee','exchange_fee','return_address','deliver','deliver_fee','deliver_no_go','deliver_fee_diff','created',)

class Product_thumnailAdmin(admin.ModelAdmin):
    fields = ['pd_image','product']
    list_display = ('id','pd_image','product')

class Product_detail_imagesAdmin(admin.ModelAdmin):
    fields = ['pd_detail_image','product']
    list_display = ['id','pd_detail_image','product']

class Product_optionsAdmin(admin.ModelAdmin):
    fields = ['type','option_name','option_price','product']
    list_display = ['id','type', 'option_name', 'option_price', 'product']

class reviewsAdmin(admin.ModelAdmin):
    fields = ['user','product','pd_durability','pd_price','pd_design','pd_delivery','rv_image','comment','helpful']
    list_display = ('id','user','product','pd_durability','pd_price','pd_design','pd_delivery','rv_image','comment','helpful','created',)

class PD_QuestionAdmin(admin.ModelAdmin):
    fields = ['type','comment','completed','user','product']
    list_display = ('id','type','comment','completed','created','user','product',)

class PD_AnswerAdmin(admin.ModelAdmin):
    fields = ['comment','question']
    list_display = ('id','comment','created','question',)



admin.site.register(Categorys, CategorysAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Product_thumnail, Product_thumnailAdmin)
admin.site.register(Product_detail_images, Product_detail_imagesAdmin)
admin.site.register(Product_options, Product_optionsAdmin)
admin.site.register(reviews)
admin.site.register(PD_Question, PD_QuestionAdmin)
admin.site.register(PD_Answer, PD_AnswerAdmin)







# from django.contrib import admin
# from .models import User
#
# # Register your models here.
# from django.contrib.auth.admin import UserAdmin
#
# class CustomUserAdmin(UserAdmin):
#    UserAdmin.fieldsets[1][1]['fields']+=('gender','birthday','profile','message')
#
#    UserAdmin.add_fieldsets += (
#        (('Additional Info'), {'fields':('gender','birthday','profile','message')}),
#    )
#
# admin.site.register(User, CustomUserAdmin)