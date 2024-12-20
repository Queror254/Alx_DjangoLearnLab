from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    # include the router URLS for BookViewSet (all CRUD operations)
    path('', include(router.urls)),

    # 'api/books?search=king'
]