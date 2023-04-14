from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework import mixins, viewsets, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MathViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = Serializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('number', openapi.IN_QUERY, description="Integer or digit string.",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('numbers', openapi.IN_QUERY, description="List of integers or digit strings.",
                              type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER)),
        ])
    def list(self, request, pk=None, **kwargs):
        result: int = 0
        self.validate_query_params(request)

        if 'numbers' in request.query_params:
            numbers: list = request.GET.getlist('numbers')

            if len(numbers) == 1 and isinstance(numbers[0], str):
                numbers = numbers[0].split(',')

            self.validate_numbers(numbers)
            result = self.get_least_common_multiple(numbers)

        if 'number' in request.query_params:
            number: int = request.query_params['number']
            self.validate_number(number)
            result = self.add_one(number)

        return Response({'result': result}, status=status.HTTP_200_OK)

    @staticmethod
    def get_least_common_multiple(numbers: list) -> int:

        numbers = [int(number) for number in numbers]

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        def lcm(a, b):
            return a * b // gcd(a, b)

        result = numbers[0]
        for i in range(1, len(numbers)):
            result = lcm(result, numbers[i])

        return result

    @staticmethod
    def add_one(number: int) -> int:
        return int(number) + 1

    @staticmethod
    def validate_numbers(numbers: list) -> None:

        if not isinstance(numbers, list):
            raise ValidationError({'numbers': 'Must be a list of integers or digit strings.'})

        if not numbers:
            raise ValidationError({'numbers': 'Cannot be empty.'})

        if not all(map(lambda x: str(x).isdigit(), numbers)):
            raise ValidationError({'numbers': 'List must contain only integers or digit strings.'})

    @staticmethod
    def validate_number(number) -> None:
        try:
            int(number)
        except ValueError:
            raise ValidationError({'number': 'Must be integer.'})

    @staticmethod
    def validate_query_params(request) -> None:
        if all(param in request.query_params for param in ['number', 'numbers']):
            raise ValidationError({'error': "You can\'t use both parameters at the same time."})

        if all(param not in request.query_params for param in ['number', 'numbers']):
            raise ValidationError({'error': "You must use one of the 'number' or 'numbers' parameters."})


