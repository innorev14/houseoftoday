from django.urls import path
from .api_views import *

urlpatterns = [
    path('delete/<int:pk>/', UserDeleteView.as_view()),
    path('detail/<int:pk>/', UserDetailView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('list/', UserListView.as_view()),
]
