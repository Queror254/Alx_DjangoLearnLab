from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookTests(APITestCase):
    
    def setUp(self):
        # Create a user for testing authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')

        # Create a sample Book instance
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2022
        }
        self.book = Book.objects.create(**self.book_data)

        # Define URLs for the API endpoints
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])
        self.book_create_url = reverse('book-create')

    # Test CRUD operations
    def test_create_book(self):
        # Test creating a book as an authenticated user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.book_create_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])
    
    def test_read_book(self):
        # Test reading a book (Detail View)
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        # Test updating a book as an authenticated user (admin)
        self.client.login(username='admin', password='adminpassword')
        updated_data = {'title': 'Updated Test Book'}
        response = self.client.put(self.book_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])

    def test_delete_book(self):
        # Test deleting a book as an authenticated admin user
        self.client.login(username='admin', password='adminpassword')
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_unauthenticated_user_create(self):
        # Test that an unauthenticated user cannot create a book
        response = self.client.post(self.book_create_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorized_user_update(self):
        # Test that a non-admin user cannot update a book
        self.client.login(username='testuser', password='testpassword')
        updated_data = {'title': 'Unauthorized Update'}
        response = self.client.put(self.book_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test filtering and searching functionality
    def test_book_search(self):
        # Test searching for books
        response = self.client.get(self.book_list_url, {'search': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')
    
    def test_book_filter(self):
        # Test filtering books by a specific field (e.g., by author)
        response = self.client.get(self.book_list_url, {'author': 'Test Author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_book_ordering(self):
        # Test ordering books by a specific field (e.g., by title)
        response = self.client.get(self.book_list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['title'] <= response.data[1]['title'])

    # Test for Permissions (admin-only operations)
    def test_admin_permissions_for_update_and_delete(self):
        # Ensure that only admin users can update and delete
        self.client.login(username='admin', password='adminpassword')
        response = self.client.put(self.book_detail_url, {'title': 'Admin Updated Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Test that a regular user cannot delete or update
        self.client.login(username='testuser', password='testpassword')
        response = self.client.put(self.book_detail_url, {'title': 'Not Allowed Title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
