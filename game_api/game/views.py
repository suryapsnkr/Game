from django.shortcuts import render
from rest_framework import viewsets
from .models import Game, PlayerScore
from .serializers import GameSerializer, PlayerScoreSerializer

# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerScoreViewSet(viewsets.ModelViewSet):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
