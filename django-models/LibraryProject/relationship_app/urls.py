from .views import views
from django.urls import path

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view for listing all books
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
]
