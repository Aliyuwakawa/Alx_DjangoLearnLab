from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create some test data
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2021)

    def test_create_book(self):
        # Test book creation
        url = reverse('book-create')
        data = {'title': 'Book Three', 'author': 'Author C', 'publication_year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_books(self):
        # Test retrieving all books
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Initially, there are 2 books

    def test_update_book(self):
        # Test updating a book
        url = reverse('book-update')
        data = {'id': self.book1.id, 'title': 'Updated Title', 'author': 'Updated Author'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        # Test deleting a book
        url = reverse('book-delete')
        data = {'id': self.book1.id}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only one book remains

    def test_filter_books(self):
        # Test filtering books by title
        url = reverse('book-list')
        response = self.client.get(url + '?title=Book One', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book matches the filter

    def test_search_books(self):
        # Test searching books by title
        url = reverse('book-list')
        response = self.client.get(url + '?search=Book', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books match the search

    def test_order_books(self):
        # Test ordering books by publication_year
        url = reverse('book-list')
        response = self.client.get(url + '?ordering=publication_year', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')  # Book One is first by year

    def test_permissions(self):
        # Test permissions: unauthenticated users can't create, update, or delete books
        self.client.logout()
        url = reverse('book-create')
        data = {'title': 'Book Three', 'author': 'Author C', 'publication_year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

