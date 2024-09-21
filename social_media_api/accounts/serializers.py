from rest_framework import serializers
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # This will automatically refer to your custom user model
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
