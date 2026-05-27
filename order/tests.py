from django.test import TestCase
from product.models import Product
from .serializers import OrderSerializer

class OrderSerializerTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Teste', price=10, stock=1)

    def test_order_serializer(self):
        data = {'product': self.product.id, 'quantity': 2}
        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid())