from django.urls import path
from .views import *

urlpatterns = [
    path('category/list/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    path('product/list/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    path('product_thumnail/list/', ThumnailListView.as_view()),
    path('product_thumnail/<int:pk>/', ThumnailDetailView.as_view(), name='product_thumnail_detail'),

    path('product_detail_image/list/', DetailImageListView.as_view()),
    path('product_detail_image/<int:pk>/', DetailImageDetailView.as_view(), name='product_detail_image'),

]
