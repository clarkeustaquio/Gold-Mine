from django.contrib import admin
from .models import GameGenerator, Box, MaximumClick, LeaderBoard
# Register your models here.

admin.site.register(GameGenerator)
admin.site.register(Box)
admin.site.register(MaximumClick)
admin.site.register(LeaderBoard)
