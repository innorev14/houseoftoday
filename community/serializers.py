from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *

class PhotoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()

    class Meta:
        model = Photo
        fields = ['author', 'image', 'hit_count', 'like_count', 'scrap_count', 'comment_count', 'text']

    def get_comments(self, photo):
        first_comment = PhotoComment.objects.filter(photo=photo)[0:1]
        serializer = PhotoCommentSerializer(instance=first_comment, many=True)
        return serializer.data