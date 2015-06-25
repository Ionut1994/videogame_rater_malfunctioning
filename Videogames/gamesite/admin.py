from django.contrib import admin
from .models import Game
from .models import Rating

admin.site.register(Game)
admin.site.register(Rating)
