from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['author', 'image', 'hit_count', 'like_count', 'scrap_count', 'comment_count', 'text']