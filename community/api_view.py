from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny

class PhotoListAPIView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (AllowAny,)