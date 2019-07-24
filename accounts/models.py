from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):
    TYPE_DJANGO, TYPE_KAKAO, TYPE_GOOGLE, TYPE_NAVER = 'django', 'kakao', 'google', 'naver'
    CHOICES_TYPE = (
        (TYPE_KAKAO, '카카오'),
        (TYPE_GOOGLE, '구글'),
        (TYPE_NAVER, '네이버'),
    )
    type = models.CharField('유형', choices=CHOICES_TYPE, max_length=12, default=TYPE_DJANGO)
    unique_user_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField('이메일', unique=True, blank=True, null=True)
    gender = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    profile = models.ImageField(upload_to='user_image/profile/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.username+"("+self.type+")"
