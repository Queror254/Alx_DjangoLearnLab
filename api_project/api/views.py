from rest_framework import generics, viewsets, filters
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

#custom view using mixins
class myView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        #view logic
        return Book.objects.filter(title="b2b")

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    #'api/books?search=king
    ordering_fields = ['title', 'author']
    #'api/books?ordering=king

class BookListx(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(author=user)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
