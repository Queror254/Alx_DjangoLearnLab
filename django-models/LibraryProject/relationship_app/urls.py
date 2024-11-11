from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='relationship_app/logout'),

    path('admin/', admin_view, name='admin_view'), # type: ignore
    path('librarian/', librarian_view, name='librarian_view'),# type: ignore
    path('member/', member_view, name='member_view'),# type: ignore

        path('add_book/', add_book_view, name='add_book'),# type: ignore
    path('edit_book/', edit_book_view, name='edit_book'),# type: ignore
    path('delete/', delete_book_view, name='delete_book'),# type: ignore
    path('books/', views.booklistView, name='list_books'),
    path('library/<int:pk>/', views.libraryDetailView.as_view(), name='library_detail'),
]
