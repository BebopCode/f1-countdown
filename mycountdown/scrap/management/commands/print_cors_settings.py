from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Prints the CORS allowed origins'

    def handle(self, *args, **kwargs):
        self.stdout.write("CORS Allowed Origins:")
        if hasattr(settings, 'CORS_ALLOWED_ORIGINS'):
            for origin in settings.CORS_ALLOWED_ORIGINS:
                self.stdout.write(f"  {origin}")
        elif getattr(settings, 'CORS_ALLOW_ALL_ORIGINS', False):
            self.stdout.write("  All origins are allowed.")
        else:
            self.stdout.write("  No specific CORS settings found.")
