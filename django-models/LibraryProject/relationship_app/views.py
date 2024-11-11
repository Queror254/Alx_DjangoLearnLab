from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm # type: ignore


@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', login_url='no_permission')
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books after adding
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit a book (requires 'can_change_book' permission)
@permission_required('relationship_app.can_change_book', login_url='no_permission')
def edit_book_view(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books after editing
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# View to delete a book (requires 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book', login_url='no_permission')
def delete_book_view(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the list of books after deletion
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# No permission view for unauthorized access attempts



def booklistView(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class libraryDetailView(DetailView):
    models = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'