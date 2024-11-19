from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# Home View
def home(request):
    return render(request, 'home.html')

# View a book (requires can_view permission)
@permission_required('app_name.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

# Create a book (requires can_create permission)
@permission_required('app_name.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        publication_year = request.POST['publication_year']
        Book.objects.create(title=title, author=author, publication_year=publication_year)
    return render(request, 'create_book.html')

# Edit a book (requires can_edit permission)
@permission_required('app_name.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_year = request.POST['publication_year']
        book.save()
    return render(request, 'edit_book.html', {'book': book})

# Delete a book (requires can_delete permission)
@permission_required('app_name.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'book_deleted.html')
