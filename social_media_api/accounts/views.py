from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated


class UserRegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user
