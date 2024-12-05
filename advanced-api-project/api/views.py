from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework



# List of Books (GET request)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'author']  # Fields you want to search by
    ordering_fields = ['title', 'publication_year']  # Fields you want to order by
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only for unauthenticated users

# Book Detail View (GET request for a single book)
class BookDetailView(generics.RetrieveAPIView):  # Changed from List to Retrieve
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only for unauthenticated users

# Create a new Book (POST request)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']  # Update search fields as per your model fields
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

# Update an existing Book (PUT request)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admin users can update

# Delete an existing Book (DELETE request)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admin users can delete