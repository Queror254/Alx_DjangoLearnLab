from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})


# Home View
def home(request):
    return render(request, 'home.html')

# Book list view
def book_list(request):
    # Retrieve all books from the database
    books = Book.objects.all()

    return render(request, 'bookshelf/book_list.html', {'books': books})

# Single book detail view
def book_detail(request, book_id):
    # Get a specific book by ID or return a 404 if it doesn't exist
    book = get_object_or_404(Book, id=book_id)

    return render(request, 'bookshelf/book_detail.html', {'book': book})

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
