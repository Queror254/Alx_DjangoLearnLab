from . import views
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path

urlpatterns = [

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Registration page
    path('register/', views.register, name='register'),
    
    # Login page (using LoginView)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html', next_page='/auth/profile/'), name='login'),
    
    # Logout page (using LogoutView)
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('profile/', views.profile, name='profile'),

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
]
