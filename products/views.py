from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.renderers import JSONRenderer


class ProductListView(generics.ListAPIView):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class CategoryListView(generics.ListAPIView):
    # renderer_classes = [JSONRenderer]

    # queryset = Categorys.objects.all().order_by('id')
    queryset = Categorys.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryDetailView(generics.RetrieveAPIView):
    # renderer_classes = [JSONRenderer]

    # queryset = Categorys.objects.all().order_by('id')
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class ThumnailListView(generics.ListAPIView):
    queryset = Product_thumnail.objects.all().order_by('id')
    serializer_class = ThumnailImageSerializer
    permission_classes = (AllowAny,)


class ThumnailDetailView(generics.RetrieveAPIView):
    queryset = Product_thumnail.objects.all()
    serializer_class = ThumnailImageSerializer
    permission_classes = (AllowAny,)


class DetailImageListView(generics.ListAPIView):
    queryset = Product_detail_images.objects.all().order_by('id')
    serializer_class = DetailImageSerializer
    permission_classes = (AllowAny,)


class DetailImageDetailView(generics.RetrieveAPIView):
    queryset = Product_detail_images.objects.all()
    serializer_class = DetailImageSerializer
    permission_classes = (AllowAny,)
