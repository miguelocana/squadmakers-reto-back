from rest_framework.routers import DefaultRouter

from api.views.joke import JokeViewSet
from api.views.math import MathViewSet


router = DefaultRouter()
router.register(r'jokes', JokeViewSet, basename='jokes')
router.register(r'math', MathViewSet, basename='math')
urlpatterns = router.urls
