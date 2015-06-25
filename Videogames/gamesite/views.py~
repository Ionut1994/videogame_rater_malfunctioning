from django.shortcuts import render
from django.utils import timezone
from .models import Game
from .models import Rating


def game_list(request):
    games = Game.objects.all()
    return render(request, 'gamesite/game_list.html', {'games': games})

