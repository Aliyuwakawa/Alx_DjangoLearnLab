from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegisterView, ProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),  # Make sure this is correct
    path('login/', obtain_auth_token, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]

