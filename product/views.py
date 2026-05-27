from rest_framework import viewsets, pagination
from .models import Product
from .serializers import ProductSerializer

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination