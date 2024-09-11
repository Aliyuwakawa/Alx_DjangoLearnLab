from django.urls import path
from . import views  # Import the views from the current app

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),  # List all books
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),  # Update a book (without ID)
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # Delete a book (without ID)
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Retrieve a book by ID
]

