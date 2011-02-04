from django.core.management.base import BaseCommand, CommandError
from mynock.feeds.models import Feed

class Command(BaseCommand):
    args = ''
    help = 'Scans feeds for new entries.'

    def handle(self, *args, **options):
        for feed in Feed.objects.all():
        	for item in feed.get_new_items():
        		self.stdout.write("Downloaded %s from %s\n" % (item.filename, feed.url))