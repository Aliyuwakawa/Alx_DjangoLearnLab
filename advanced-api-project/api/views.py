from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters  # Import Django Filter
from rest_framework import filters as drf_filters  # For search and ordering
from .models import Book
from .serializers import BookSerializer

# Define a filter set for the Book model
class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],  # Filter by exact title or partial match (case-insensitive)
            'author': ['exact', 'icontains'],
            'publication_year': ['exact', 'gte', 'lte'],  # Filter by year (exact, greater than, less than)
        }

# List and Create View for Books with filtering, searching, and ordering
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    filterset_class = BookFilter  # Use the custom BookFilter class for filtering
    search_fields = ['title', 'author']  # Enable searching by title and author
    ordering_fields = ['title', 'publication_year']  # Enable ordering by title or publication year

# Detail, Update, and Delete Views for Books
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
