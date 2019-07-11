from .serializers import UserListSerializer, UserCreateSerializer ,UserModifySerializer, UserDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import AllowAny

"""
List : GET
Create : POST
Retrieve : GET
Update : PUT, PATCH
Destroy : Delete
"""


class UserListView(generics.ListAPIView):
   # renderer_classes = [JSONRenderer] # JSON 형식으로만 받고 싶은 경우
   queryset = get_user_model().objects.all()
   serializer_class = UserListSerializer
   filterset_fields = ('email', 'username')

   def get_queryset(self):
       queryset = super().get_queryset()
       if not self.request.user.is_staff:
           queryset = queryset.filter(pk=self.request.user.id)
       return queryset

class UserCreateView(generics.CreateAPIView):
   serializer_class = UserCreateSerializer
   # 회원가입시 토근권한이 없어도 가입할 수 있도록 권한 부여
   permission_classes = (AllowAny,)

class UserUpdateView(generics.UpdateAPIView):
   queryset = get_user_model().objects.all()
   serializer_class = UserModifySerializer

class UserDetailView(generics.RetrieveAPIView):
   queryset = get_user_model().objects.all()
   serializer_class = UserDetailSerializer

class UserDeleteView(generics.DestroyAPIView):
   queryset = get_user_model().objects.all()