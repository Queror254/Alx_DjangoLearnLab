from django.contrib import admin
from .models import Book

#admin config for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

#register the Book model
admin.site.register(Book)
