from django.contrib.auth import get_user_model

User = get_user_model()

# Email Login Authentication
class EmailBackend:
    def authenticate(self, request, email, password):
        """

        :param request:
        :param email: 유저 이메일
        :param password: 유저 패스워드
        :return: user object
        """
        try:
           user = User.objects.get(email=email)

        except User.DoesNotExist:
           return None

        # 패스워드 맞는지 검사
        if user.check_password(password):
           return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# Social Login Authentication
class SocialLoginBackend:
    def authenticate(self, request, type, unique_user_id, username, email, social_profile):
        """

        :param request:
        :param type: 오늘의 집 로그인인지, 소셜로그인인지
        :param unique_user_id: 클라이언트가 보내준 Unique ID
        :param username: 클라이언트가 보내준 유저 정보 중 username
        :param email: 클라이언트가 보내준 유저 정보 중 email
        :param social_profile: 클라이언트가 보내준 유저 정보 중 profile image
        :return: User object
        """
        # 추가정보 필요없이 유저를 생성하면 되는 경우
        user, user_created = User.objects.update_or_create(
            type=type,
            unique_user_id=unique_user_id,
            defaults={
                'username': username,
                'email': email,
                'social_profile': social_profile,
            },
        )
        return user



    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

