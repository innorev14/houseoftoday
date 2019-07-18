from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.renderers import JSONRenderer


class ProductListView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class ProductDetailView(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)


class CategoryListView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryDetailView(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
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

