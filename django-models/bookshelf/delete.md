from bookshelf.models import Book
book = Book.objects.all()
book.delete()

Output:
<QuerySet []>
