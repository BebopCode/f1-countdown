# Generated by Django 4.2.13 on 2024-08-31 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0003_racemodel_location_alter_racemodel_qualifying_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamLeaderBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField()),
                ('position', models.IntegerField()),
                ('team', models.CharField(max_length=100)),
                ('points', models.CharField(max_length=100)),
            ],
        ),
    ]
