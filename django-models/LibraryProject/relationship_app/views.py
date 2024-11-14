from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .models import Book
from .models import Library

#Home View
def home(request):
    return render(request, 'home.html')

#Role-based Views

# Utility function to check the role
def is_admin(user):
    return user.userprofile.role.lower() == 'admin'

def is_librarian(user):
    return user.userprofile.role.lower() == 'librarian'

def is_member(user):
    return user.userprofile.role.lower() == 'member'

# Admin view (only accessible by Admin users)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view (only accessible by Librarian users)
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view (only accessible by Member users)
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

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
            return redirect('')  # Redirect to the home page or other page
        else:
            return render(request, 'relationship_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'relationship_app/login.html')

# User Logout view
@login_required 
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

@login_required
def profile(request):
    # Get the user profile data (you can add more fields if needed)
    user_profile = request.user.userprofile
    context = {
        'user': request.user,
        'profile': user_profile,
    }
    return render(request, 'relationship_app/profile.html', context)



######################

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    models = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'