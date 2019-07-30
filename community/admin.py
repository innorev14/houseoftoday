from django.contrib import admin
from .models import *

class PhotoAdmin(admin.ModelAdmin):
    fields = ['category', 'created', 'image', 'axis_left', 'axis_top',
              'product_image', 'product_id', 'text', 'author', 'author_profile_image',
              'author_profile_comment', 'like_count', 'scrap_count', 'hit_count', 'comment_count']
    list_display = ['id', 'author', 'text']

class TagAdmin(admin.ModelAdmin):
    fields = ['photo', 'word']
    list_display = ['id', 'word']

class PhotoCommentAdmin(admin.ModelAdmin):
    fields = ['photo', 'author', 'author_profile_image', 'text', 'created']
    list_display = ['id', 'author', 'text', 'created']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PhotoComment, PhotoCommentAdmin)

