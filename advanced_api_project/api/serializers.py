from rest_framework import serializers
from .models import Author, Book

# BookSerializer serializes the Book model fields and ensures the publication year is valid.
# AuthorSerializer nests the BookSerializer to serialize all books related to an author.


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year']

    def validate_publication_year(self, value):
        import datetime
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
