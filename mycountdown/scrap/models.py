from django.db import models

class RaceModel(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length= 100, default='')
    qualifying = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    sprint = models.CharField(max_length=100,null=True)
    sprint_shootout = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"Race - {self.title} {self.location}, Race time - {self.race}, Qualifying time - {self.qualifying}"

class LeaderBoard(models.Model):
    update_time = models.DateTimeField()
    position = models.IntegerField()
    driver = models.CharField(max_length=100)
    car = models.CharField(max_length=100)
    points = models.IntegerField()
