from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, PlayerScoreViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'scores', PlayerScoreViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
