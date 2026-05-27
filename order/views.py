from rest_framework import viewsets, pagination
from .models import Order 
from .serializers import OrderSerializer 

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer