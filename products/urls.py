from django.urls import path
from .views import *

urlpatterns = [
   path('category/list/', CategoryListView.as_view()),
]