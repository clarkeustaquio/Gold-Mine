from django.urls import path
from . import views
from random import random

from django.conf import settings
from django.conf.urls.static import static

app_name = 'gold_app'

def generate_random():
    random_number = str(random())
    random_number = random_number.replace(".", "")
    return random_number

urlpatterns = [
    path('', views.index, name='index'),
    path('user_select/<int:id>/', views.user_select, name='user_select'),
    path('leaderboard/', views.leader_board, name='leader_board'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)