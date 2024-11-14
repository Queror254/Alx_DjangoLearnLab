from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book
from .models import Library

# Create your views here.
# User Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or other page
        else:
            return render(request, 'relationship_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'relationship_app/login.html')

# User Logout view
@login_required 
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


def home(request):
    return render(request, 'home.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    models = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'