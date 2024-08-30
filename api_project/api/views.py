from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Book  # Adjust the import based on your model's location
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# api/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


