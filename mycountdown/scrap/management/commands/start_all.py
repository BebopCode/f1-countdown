from django.core.management.base import BaseCommand
from django.core.management import call_command
import subprocess
import threading
import time

class Command(BaseCommand):
    help = 'Starts the server and runs upcoming_race and scrap_leaderboard after the server is up'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting server...')
        server_thread = threading.Thread(target=self.start_server)
        server_thread.start()

        self.stdout.write('Waiting for the server to start...')
        time.sleep(10)  # Wait for 10 seconds to ensure the server is up

        self.stdout.write('Running additional commands...')
        call_command('upcoming_race')
        self.stdout.write('upcoming_race command executed.')

        call_command('scrap_leaderboard')
        self.stdout.write('scrap_leaderboard command executed.')

        # Wait for the server thread to finish
        server_thread.join()

    def start_server(self):
        subprocess.run(['python', 'manage.py', 'runserver', '0.0.0.0:8000'])