from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import *
from .serializers import CustomUserSerializer


class CustomerUserView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
