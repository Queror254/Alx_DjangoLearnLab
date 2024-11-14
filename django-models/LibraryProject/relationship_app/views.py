from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian

# Create your views here.
def home(request):
    return render(request, 'home.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    models = Library
    template_name = 'relationship_app/library_books.html'
    context_object_name = 'library'