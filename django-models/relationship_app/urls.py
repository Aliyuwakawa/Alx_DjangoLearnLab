from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Registration view
    path('register/', views.register, name='register'),

    # Login view using Django's built-in LoginView
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view using Django's built-in LogoutView
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

