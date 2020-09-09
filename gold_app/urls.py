from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'gold_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('user_select/<int:id>/', views.user_select, name='user_select'),
    path('leaderboard/', views.leader_board, name='leader_board'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)