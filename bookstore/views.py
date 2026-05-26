from rest_framework import viewsets
from .models import Book, Order
from .serializers import BookSerializer, OrderSerializer
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


def home(request):
    return HttpResponse("<h1>Bem-vinda à Bookstore API!</h1><p>Acesse <a href='/api/books/'>aqui</a> para ver os livros.</p>")


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)