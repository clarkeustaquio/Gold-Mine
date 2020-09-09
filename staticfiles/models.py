import random

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.


class GameGenerator(models.Model):
    game = models.CharField(max_length=10, default='Gold Mine')
    golds = models.IntegerField(default=10)
    bombs = models.IntegerField(default=30)
    diamonds = models.IntegerField(default=1)
    max_platform = models.IntegerField(default=100)


    def _generateGame(self):
        random_ids = set()
        while len(random_ids) < self.max_platform:
            random_ids.add(
                random.randint(
                    self.max_platform, 
                    self.max_platform * 10,
                )
            )

        count = 0
        for random_id in random_ids:
            if count < self.golds:
                Box.objects.create(
                    id=random_id,
                    game=self,
                    name='Gold',
                )
            elif count >= self.golds and count < (self.bombs + self.golds):
                Box.objects.create(
                    id=random_id,
                    game=self,
                    name='Bomb',
                )
            elif count == (self.bombs + self.golds):
                Box.objects.create(
                    id=random_id,
                    game=self,
                    name='Diamond',
                )
            elif count < self.max_platform:
                Box.objects.create(
                    id=random_id,
                    game=self,
                    name='None',
                )
            count += 1

    def __str__(self):
        return self.game

    def save(self, *args, **kwargs):
        super(GameGenerator, self).save(*args, **kwargs)
        self._generateGame()

class Box(models.Model):
    game = models.ForeignKey(GameGenerator, on_delete=models.CASCADE, db_constraint=False)
    name = models.CharField(max_length=10)
    
    def clean(self):
        model = self.__class__
        if model.objects.count() >= self.game.max_platform:
            raise ValidationError('Maximum Box: {}'.format(self.game.max_platform))

    def __str__(self):
        return self.name

class MaximumClick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clicks = models.IntegerField(default=10)
    golds = models.IntegerField(default=0)
    diamonds = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)

class LeaderBoard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.user, self.score)