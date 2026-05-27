from django.test import TestCase
from .serializers import ProductSerializer

class ProductSerializerTest(TestCase):
    def test_serializer_with_valid_data(self):
        data = {'name': 'Teste', 'price': '10.00', 'stock': 5}
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())