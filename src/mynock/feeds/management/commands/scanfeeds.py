from django.core.management.base import BaseCommand, CommandError
from mynock.feeds.models import Feed

class Command(BaseCommand):
    args = ''
    help = 'Scans feeds for new entries.'

    def handle(self, *args, **options):
        self.stdout.write('Retrieving new items for feeds\n')