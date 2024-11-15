from django.contrib import admin
from .models import UserProfile, Book, Author, Librarian, Library

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(Author)


