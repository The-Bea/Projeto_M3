from django.test import TestCase
from .serializers import BookSerializer
from .factories import BookFactory

class BookSerializerTest(TestCase):
    def test_serializer_contains_expected_fields(self):
        book = BookFactory()
        serializer = BookSerializer(instance=book)
        data = serializer.data

        self.assertEqual(set(data.keys()), set(['id', 'title', 'author', 'price', 'edition']))