# Generated by Django 3.1.1 on 2020-09-04 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gold_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('game', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='gold_app.gamegenerator')),
            ],
        ),
        migrations.RemoveField(
            model_name='diamond',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gold',
            name='game',
        ),
        migrations.DeleteModel(
            name='Bomb',
        ),
        migrations.DeleteModel(
            name='Diamond',
        ),
        migrations.DeleteModel(
            name='Gold',
        ),
    ]