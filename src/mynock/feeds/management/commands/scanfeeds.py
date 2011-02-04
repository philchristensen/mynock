from django.core.management.base import BaseCommand, CommandError
from mynock.feeds.models import Feed

class Command(BaseCommand):
    args = ''
    help = 'Scans feeds for new entries.'

    def handle(self, *args, **options):
        for feed in Feed.objects.filter(active=True):
            if(feed.has_new_items()):
                self.stdout.write('Retrieving new items for feed: %s' % feed.url)
            else:
                self.stdout.write('Ignoring feed: %s' % feed.url)