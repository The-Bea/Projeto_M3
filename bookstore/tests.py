from django.test import TestCase
from .factories import BookFactory
from .serializers import BookSerializer


class BookSerializerTest(TestCase):
    def test_serializer_contains_expected_fields(self):
        book = BookFactory()
        serializer = BookSerializer(instance=book)
        data = serializer.data

        self.assertEqual(set(data.keys()), set(['id', 'title', 'author', 'price', 'edition']))

    def test_serializer_with_invalid_data(self):

            invalid_data = {
                'title': 'Livro Teste',
                'author': 'Autor Teste',
                'price': 'valor_errado', 
                'edition': 1
            }
            serializer = BookSerializer(data=invalid_data)

            self.assertFalse(serializer.is_valid())
            self.assertIn('price', serializer.errors)