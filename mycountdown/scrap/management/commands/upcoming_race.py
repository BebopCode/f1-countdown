import json
from scrap.models import RaceModel
from django.core.management.base import BaseCommand
from datetime import datetime
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
import os
class Command(BaseCommand):
    upcoming_races = []
    time_now = timezone.now()
    def convert_time():
        #TODO
        pass 

    def extract_races_from_json(self):
        RaceModel.objects.all().delete()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)
        json_file_path = os.path.join(current_dir, 'race_data.json')
        print(self.time_now)
        with open(json_file_path,'r') as races_file:
            races = json.load(races_file)
            for race in races["races"]:
                sprint = ''
                sprint_qualifying = ''
                if "sprintQualifying" in race["sessions"]:
                    sprint = race["sessions"]["sprint"]
                    sprint_qualifying = race["sessions"]["sprintQualifying"]

                race_model_data = RaceModel(
                    title = race["name"]+' Grand Prix',
                    location = race["location"],
                    qualifying = race["sessions"]["qualifying"],
                    race = race["sessions"]["gp"],
                    sprint = sprint,
                    sprint_shootout = sprint_qualifying
                )
                race_model_data.save()

            all_race_data = RaceModel.objects.all()
            for race_data in all_race_data:
                print(race_data)

    def handle(self, *args, **options):
        self.extract_races_from_json()
        pass




        