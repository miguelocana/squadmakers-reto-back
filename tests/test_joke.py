import pytest

from django.urls import reverse
from rest_framework import status
from model_bakery import baker

from api.models import Joke


@pytest.mark.django_db
class TestJoke:
    list_url = 'jokes-list'
    create_url = list_url
    update_url = 'jokes-detail'
    delete_url = update_url

    def test_list_without_param(self, client):
        objs = baker.make(Joke, _quantity=3)
        jokes = [joke.joke for joke in objs]

        response = client.get(reverse(self.list_url))
        assert response.status_code == status.HTTP_200_OK
        assert response.json() in jokes

    def test_list_when_there_are_no_jokes(self, client):
        response = client.get(reverse(self.list_url))

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_list_with_chuck_param(self, client):
        response = client.get(reverse(self.list_url), {'param': 'chuck'})
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), str)

    def test_list_with_dad_param(self, client):
        response = client.get(reverse(self.list_url), {'param': 'chuck'})
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), str)

    def test_list_with_invalid_param(self, client):
        response = client.get(reverse(self.list_url), {'param': 'no_chuck_nor_dad'})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_ok(self, client):
        joke = 'This is a joke'

        response = client.post(reverse(self.create_url), {'joke': joke})
        json = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert 'id' in json
        assert 'joke' in json
        assert json['joke'] == joke

    def test_update_ok(self, client):
        obj = baker.make(Joke)
        joke = 'This is a NEW joke'

        response = client.put(reverse(self.update_url, kwargs={'pk': obj.id}), {'joke': joke})
        json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert 'id' in json
        assert 'joke' in json
        assert json['joke'] == joke

    def test_delete_ok(self, client):
        obj = baker.make(Joke)

        response = client.delete(reverse(self.delete_url, kwargs={'pk': obj.id}))
        assert response.status_code == status.HTTP_204_NO_CONTENT
