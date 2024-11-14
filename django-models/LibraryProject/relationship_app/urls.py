from .views import views
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path

urlpatterns = [

    # Registration page
    path('register/', views.register, name='register'),
    
    # Login page (using LoginView)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout page (using LogoutView)
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
]
