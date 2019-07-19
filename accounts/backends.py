from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomUserBackend(ModelBackend):
   def authenticate(self, request, username=None, password=None, **kwargs):
       user = super().authenticate(request, username, password, **kwargs)

       if user:
           return user

       # id 로그인 실패 상황
       # email 로그인 시도
       UserModel = get_user_model()
       # 원래 id 로그인 처리를 할 때 username이 넘어왔을 경우
       # email 변수에 새로 값을 할당하려고
       email = username
       if email is None:
           email = kwargs.get(UserModel.EMAIL_FIELD, kwargs.get('email'))
       try:
           user = UserModel._default_manager.get(email=email)
       except UserModel.DoesNotExist:
           # Run the default password hasher once to reduce the timing
           # difference between an existing and a nonexistent user (#20760).
           UserModel().set_password(password)
       else:
           if user.check_password(password) and self.user_can_authenticate(user):
               return user