from django.urls import path
from .api_views import *

urlpatterns = [
    path('category/list/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),

    path('product/list/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),





    # path('thumnail/list/', ThumnailListView.as_view()),
    # path('thumnail/<int:pk>/', ThumnailDetailView.as_view()),
    #
    # path('detail_image/list/', DetailImageListView.as_view()),
    # path('detail_image/<int:pk>/', DetailImageDetailView.as_view()),
    #
    # path('option/list/', ProductOptionListView.as_view()),
    # path('option/<int:pk>/', ProductOptionDetailView.as_view()),
]
