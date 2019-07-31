from rest_framework import serializers
from .models import User

from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

# 유저 목록에 출력될 형식 지정
class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['id', 'type', 'username', 'email', 'social_profile', 'gender', 'birthday', 'message', 'profile']

# 회원 가입할 때 필요한 필드들에 관한 Serializer
class UserCreateSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['email', 'password', 'username']

   def create(self, validated_data):
       user = User.objects.create(**validated_data)
       user.set_password(validated_data.get('password'))
       user.save()
       return user # create는 방금 만든 오브젝트를 반드시 리턴해줘야 한다.


class UserModifySerializer(serializers.ModelSerializer):

   class Meta:
       model = User
       fields = ['username', 'email', 'gender', 'birthday', 'message', 'profile']
       read_only_fields = ['email']

   # 기존의 update 함수를 오버라이딩해서 사용한다.
   # password만 수정하고 다른 정보는 빈칸으로 둘 경우, 다른 정보가 빈칸으로 저장될 수 있다.
   # 따라서 기존의 update 함수 내용을 오버라이딩해서 사용하도록 한다.
   def update(self, instance, validated_data):
       for key, value in validated_data.items():
           if key == 'password' and value:
               instance.set_password(value)
           elif value:
               setattr(instance, key, value)
       instance.save()
       return instance

class UserDetailSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['id', 'username', 'email', 'gender', 'birthday', 'message', 'profile']

# Email Login
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

# Social Login
class SocialAuthTokenSerializer(serializers.Serializer):
    type = serializers.CharField(label=_("Type"))
    unique_user_id = serializers.CharField(label=_("UniqueID"))
    username = serializers.CharField(label=_("Username"))
    email = serializers.CharField(label=_("Email"))
    social_profile = serializers.CharField(label=_("Social_profile"), allow_blank=True)

    def validate(self, attrs):
        type = attrs.get('type')
        unique_user_id = attrs.get('unique_user_id')
        username = attrs.get('username')
        email = attrs.get('email')
        social_profile = attrs.get('social_profile')

        if type and unique_user_id and username and email:
            user = authenticate(request=self.context.get('request'),
                                type=type, unique_user_id=unique_user_id,
                                username=username, email=email, social_profile=social_profile)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "type" and "UniqueID" and "username" and "email".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs