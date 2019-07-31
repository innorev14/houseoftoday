from django.urls import path
from .api_views import *

urlpatterns = [
    path('photo/', PhotoListAPIView.as_view()),
    path('photo/<int:pk>', PhotoDetailAPIView.as_view()),
]
