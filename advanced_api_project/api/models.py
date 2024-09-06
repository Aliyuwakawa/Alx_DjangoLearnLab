from django.db import models

# Author model represents a writer of books. Each author can have multiple books (One-to-Many relationship).
# Book model represents individual books with a title, publication year, and an associated author.


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

