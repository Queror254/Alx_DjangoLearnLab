from LibraryProject.relationship_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('books/', views.list_books, name='list_books'),  # Function-based view for listing all books
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
]
