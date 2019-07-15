from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

class CategoryListView(generics.ListAPIView):
    # renderer_classes = [JSONRenderer]
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
