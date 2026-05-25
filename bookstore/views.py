from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Bem-vinda à Bookstore API!</h1><p>Acesse <a href='/api/books/'>aqui</a> para ver os livros.</p>")


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer