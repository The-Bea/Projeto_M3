import factory
from .models import Book

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=3)
    author = factory.Faker('name')
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2)
    edition = factory.Faker('random_int', min=1, max=10)