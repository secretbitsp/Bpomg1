from django.core.management.base import BaseCommand, CommandError
from finalbp.helpers import fetch_cars


class Command(BaseCommand):
    help = 'Fetch the cars list and populate in database'

    def handle(self, *args, **options):
        fetch_cars()
