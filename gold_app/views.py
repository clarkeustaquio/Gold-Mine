from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Box, MaximumClick, LeaderBoard
import random
from django.core import serializers

# Create your views here.
def index(request):
    boxs = Box.objects.all()
    boxes = [box for box in boxs]
    random.shuffle(boxes)

    context = {
        'boxes': boxes,
    }

    if request.user.is_authenticated:
        try:
            user_click = MaximumClick.objects.get(user=request.user)

        except MaximumClick.DoesNotExist:
            user_click = MaximumClick.objects.create(
                user=request.user
            )

        context['clicks'] = user_click
        context['golds'] = user_click.golds
        context['diamond'] = user_click.diamonds
        context['score'] = user_click.golds * 2 if user_click.diamonds else user_click.golds

    return render(request, 'gold_app/index.html', context)

def user_select(request, id):
    score = 0
    context = dict()
    session_id = list()
    box = Box.objects.get(id=id)

    if not MaximumClick.objects.filter(user=request.user).exists():
        user_click = MaximumClick.objects.create(
            user=request.user,
        )
        if user_click.clicks > 0:
            user_click.clicks = user_click.clicks - 1
            user_click.save()
        
    else:
        user_click = MaximumClick.objects.get(user=request.user)
        remaining = user_click.clicks - 1
        if user_click.clicks > 0:
            user_click.clicks = remaining
            user_click.save()
    
    if box.name == 'Gold':
        request.session['Gold-{}'.format(id)] = id
        user_click.golds = user_click.golds + 1
        user_click.save()
    elif box.name == 'Diamond':
        request.session['Diamond-{}'.format(id)] = id
        user_click.diamonds = user_click.diamonds + 1
        user_click.save()
    elif box.name == 'Bomb':
        request.session['Bomb-{}'.format(id)] = id
        user_click.clicks = 0
        user_click.save()
    elif box.name == 'None':
        request.session['None-{}'.format(id)] = id

    context['golds'] = user_click.golds
    context['diamond'] = user_click.diamonds
    context['click'] = user_click.clicks

    if user_click.clicks == 0:
        if user_click.diamonds:
            score = user_click.golds * 2
        else:
            score = user_click.golds

        if not LeaderBoard.objects.filter(user=request.user).exists():
            leader_board = LeaderBoard.objects.create(
                user=request.user,
                score=score
            )
        else:
            leader_board = LeaderBoard.objects.get(user=request.user)
            leader_board.score = score
            leader_board.save()

    print(score)
    for key, value in request.session.items():
        session_id.append(key)
    context['session'] = session_id

    return JsonResponse(context, safe=False, status=200, json_dumps_params={'indent': 4})

def leader_board(request):
    leader_boards = LeaderBoard.objects.order_by('-score')

    context = {
        'leader_boards': leader_boards
    }
    print(leader_boards)
    return render(request, 'gold_app/leaderboard.html', context)