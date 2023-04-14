import requests
import random

from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import mixins, viewsets, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.models import Joke
from api.serializers import JokeSerializer


class JokeViewSet(mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('param', openapi.IN_QUERY, description="Do you want a Chuck or a Dad joke?",
                              type=openapi.TYPE_STRING),
        ])
    def list(self, request, *args, **kwargs):
        joke: str = ''

        if 'param' in request.query_params:
            param: str = request.query_params['param']
            self.validate_param(param)

            if param.lower() == 'chuck':
                joke = self.get_chuck_joke()
            elif param.lower() == 'dad':
                joke = self.get_dad_joke()

        else:
            jokes = list(self.get_queryset())
            if not jokes:
                return Response('No jokes in the database.', status=status.HTTP_204_NO_CONTENT)
            joke = random.choice(jokes).joke

        return Response(joke, status=status.HTTP_200_OK)

    @staticmethod
    def get_chuck_joke() -> str:
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['value']
        else:
            raise ValidationError(f'Error obtaining joke. Server response: {response.status_code}')

    @staticmethod
    def get_dad_joke() -> str:
        url = 'https://icanhazdadjoke.com/'
        response = requests.get(url, headers={'Accept': 'application/json'})
        if response.status_code == 200:
            return response.json()['joke']
        else:
            raise ValidationError(f'Error obtaining joke. Server response: {response.status_code}')

    @staticmethod
    def validate_param(param) -> None:
        if param not in ['chuck', 'dad']:
            raise ValidationError({'param': 'Must be a choice between `Chuck` or `Dad`.'})
