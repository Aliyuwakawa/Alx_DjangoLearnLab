# api/serializers.py
from rest_framework import serializers
from .models import Book  # Adjust the import based on your model's location

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # This includes all fields of the Book model
