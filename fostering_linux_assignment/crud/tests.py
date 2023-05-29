from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookListViewTest(TestCase):
    def test_book_list_view(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')

class BookCreateViewTest(TestCase):
    def test_book_create_view(self):
        url = reverse('book_create')
        data = {
            'title': 'Test Book',
            'description': 'This is a test book',
            'page_count': 100,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Check if redirecting after successful creation
        self.assertEqual(Book.objects.count(), 1)  # Check if the book was created
        self.assertRedirects(response, reverse('book_list'))

class BookUpdateViewTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Test Book', description='This is a test book', page_count=100)
    
    def test_book_update_view(self):
        url = reverse('book_update', args=[self.book.pk])
        data = {
            'title': 'Updated Book',
            'description': 'This book has been updated',
            'page_count': 200,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Check if redirecting after successful update
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')  # Check if the book was updated
        self.assertRedirects(response, reverse('book_list'))

class BookDeleteViewTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Test Book', description='This is a test book', page_count=100)
    
    def test_book_delete_view(self):
        url = reverse('book_delete', args=[self.book.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Check if redirecting after successful deletion
        self.assertEqual(Book.objects.count(), 0)  # Check if the book was deleted
        self.assertRedirects(response, reverse('book_list'))
