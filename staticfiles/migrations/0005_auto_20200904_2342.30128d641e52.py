# Generated by Django 3.1.1 on 2020-09-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold_app', '0004_leaderboard_maximumclick'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maximumclick',
            name='clicks',
            field=models.IntegerField(default=10),
        ),
    ]
