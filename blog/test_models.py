import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_view_retorna_status_200_e_hello_world(client):

    url = reverse('home')
    

    response = client.get(url)
    

    assert response.status_code == 200
    

    assert "Hello World" in response.content.decode('utf-8')