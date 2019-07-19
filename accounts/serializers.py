from rest_framework import serializers
from .models import User

# 유저 목록에 출력될 형식 지정

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['id', 'username', 'email', 'gender', 'birthday', 'message', 'profile']

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