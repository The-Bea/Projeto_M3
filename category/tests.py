from django.test import TestCase
from .serializers import CategorySerializer

class CategorySerializerTest(TestCase):
    def test_serializer_with_valid_data(self):
        data = {'name': 'Livros'}
        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid())