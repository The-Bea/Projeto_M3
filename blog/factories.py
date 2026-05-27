import factory
from .models import Post

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    titulo = factory.Faker('sentence', nb_words=4)
    conteudo = factory.Faker('paragraph', nb_sentences=5)
    publicado = True