import os.path

from django.db import models

import feedparser, urllib2

class Feed(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def get_new_items(self):
        parser = feedparser.parse(self.url)
        for entry in parser['items']:
            filename = os.path.basename(entry['link'])
            existing = FeedItem.objects.filter(feed=self, filename=filename)
            if(existing):
                continue
            
            item = FeedItem()
            item.feed = self
            item.title = entry['title']
            item.url = entry['link']
            item.filename = item.download_attachment()
            item.save()

            yield item

class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)

    def download_attachment(self):
        data = None
        filename = os.path.basename(self.url)
        destination = os.path.join('attachments', filename)
        # this should probably replaced with a
        # subprocess call to a more capable web client
        s = urllib2.urlopen(self.url)
        f = open(destination, 'wb')
        with f:
            data = s.read(8192)
            while(data):
                f.write(data)
                data = s.read(8192)
        s.close()
        return filename