import pytest
from blog.factories import PostFactory

@pytest.mark.django_db
def test_criar_post_com_factory():
    # Usando a factory para criar um post no banco de dados de teste
    post = PostFactory(titulo="Meu Primeiro Projeto")

    assert post.id is not None
    assert post.titulo == "Meu Primeiro Projeto"
    assert post.publicado is True