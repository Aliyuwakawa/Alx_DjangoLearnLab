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

from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for adding a book
    path('add_book/', views.add_book, name='add_book'),

    # URL pattern for editing a book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),

    # URL pattern for deleting a book
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
