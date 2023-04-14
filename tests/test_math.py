import pytest

from django.urls import reverse
from rest_framework import status


class TestMath:
    list_url = 'math-list'

    @pytest.mark.parametrize('numbers, result', [
        ([4, 6, 8], 24),
        (['3', '4', '6'], 12),
        ([8, 10], 40),
    ])
    def test_numbers_ok(self, client, numbers, result):
        response = client.get(reverse(self.list_url), {'numbers': numbers})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'result': result}

    @pytest.mark.parametrize('numbers', [
        ([4.0, 6.0, 8.2]),
        ([4, 3, True]),
        ([4, 3, 'hello'])
    ])
    def test_numbers_with_non_integers(self, client, numbers):
        response = client.get(reverse(self.list_url), {'numbers': numbers})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_numbers_with_empty_list(self, client):
        response = client.get(reverse(self.list_url), {'numbers': []})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.parametrize('number, result', [(4, 5), ('3', 4)])
    def test_number_ok(self, client, number, result):
        response = client.get(reverse(self.list_url), {'number': number})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'result': result}

    @pytest.mark.parametrize('number', ['Test', 4.0, True])
    def test_number_with_non_integer(self, client, number):
        response = client.get(reverse(self.list_url), {'number': number})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_with_no_params(self, client):
        response = client.get(reverse(self.list_url))

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_with_both_params(self, client):
        response = client.get(reverse(self.list_url), {'number': 4, 'numbers': [4, 6, 8]})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
