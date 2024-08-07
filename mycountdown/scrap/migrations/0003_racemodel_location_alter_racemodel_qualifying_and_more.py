# Generated by Django 4.2.13 on 2024-07-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_leaderboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='racemodel',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='racemodel',
            name='qualifying',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='racemodel',
            name='race',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='racemodel',
            name='sprint',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='racemodel',
            name='sprint_shootout',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
