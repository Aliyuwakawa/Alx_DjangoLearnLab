from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()  # Ensure this line is included

    class Meta:
        model = get_user_model()  # Automatically refers to your custom user model
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password']
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', ''),
        )
        Token.objects.create(user=user)  # Create a token for the user
        return user
