from bookshelf.models import Books
book.delete()
books = Book.objects.all()
print(books)
# Expected Output: <QuerySet []>

