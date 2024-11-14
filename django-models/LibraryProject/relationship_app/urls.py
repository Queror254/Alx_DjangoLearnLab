from .views import list_books
from .views import LibraryDetailView
from .views import login_view
from .views import logout_view
from .views import register
from django.urls import path

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
]
