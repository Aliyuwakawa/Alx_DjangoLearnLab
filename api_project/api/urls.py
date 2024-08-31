# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Ensure this is the correct view import
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
