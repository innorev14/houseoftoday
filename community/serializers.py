from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *

# 사진 탭 댓글 관련 serializer
class PhotoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = '__all__'

class PhotoCommentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoComment
        fields = ['author_profile_image', 'author', 'text']

class PhotoSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()

    class Meta:
        model = Photo
        fields = ['id', 'author', 'image', 'hit_count', 'like_count',
                  'scrap_count', 'comment_count', 'text', 'comments']

    def get_comments(self, photo):
        first_comment = PhotoComment.objects.filter(photo=photo)[0:1]
        serializer = PhotoCommentSimpleSerializer(instance=first_comment, many=True)
        return serializer.data

class PhotoDetailSerializer(serializers.ModelSerializer):
    photo_comments = PhotoCommentSerializer(source='comments', many=True)

    class Meta:
        model = Photo
        fields = '__all__'