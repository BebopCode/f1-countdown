from django.db import models

class RaceModel(models.Model):
    title = models.CharField(max_length=100)
    qualifying = models.DateTimeField()
    race = models.DateTimeField()
    sprint = models.DateTimeField(null=True)
    sprint_shootout = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f"Race - {self.title}, Race time - {self.race}, Qualifying time - {self.qualifying}"
