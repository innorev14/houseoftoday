"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from accounts.api_views import CustomObtainAuthToken

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="House Of Today(clone) API",
        default_version='v1',
        description="1팀 WPS의 House Of Today(clone) API 문서 페이지 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="askjw123@naver.com"),
        license=openapi.License(name="1팀 WPS의 House Of Today 문서"),
    ),
    validators=['flex'], #'ssv'],
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),
    # api token
    path('get_token/', CustomObtainAuthToken.as_view()),
    # 유저 관련 페이지
    path('accounts/', include('accounts.urls')),
    # 상품 관련 페이지
    path('products/', include('products.urls')),

    # json 파일 다운로드
    path('swagger/.json/', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),

    # swagger 기능 API 문서
    path('swagger/v1/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # API 목록 문서
    path('docs/v1/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
