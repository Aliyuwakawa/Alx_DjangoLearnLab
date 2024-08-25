# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book  # Import your model or any relevant model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Replace 'Book' with the model you're using
        fields = ['title', 'author', 'published_date']  # List the fields you want in the form
