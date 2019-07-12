from rest_framework import serializers
from .models import *

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = "__all__"
