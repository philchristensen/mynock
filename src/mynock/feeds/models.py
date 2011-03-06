# mynock
# Copyright (c) 2011 Phil Christensen
#
#
# See LICENSE for details

import os.path

from django.db import models
from django.conf import settings

import feedparser, urllib2, datetime

class Feed(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    last_scan = models.DateTimeField(optional=True)
    
    def __str__(self):
        return self.url
    
    def get_new_items(self):
        self.last_scan = datetime.datetime.utcnow()
        self.save()
        
        parser = feedparser.parse(self.url)
        for entry in parser['items']:
            existing = FeedItem.objects.filter(feed=self, guid=entry['guid'])
            if(existing):
                continue
            
            item = FeedItem()
            item.feed = self
            item.guid = entry['guid']
            item.title = entry['title']
            item.url = entry['link']

            date_published = entry.get('published_parsed', entry.get('updated_parsed'))
            if date_published:
                item.pub_date = datetime.datetime(*date_published[:-3])
            else:
                item.pub_date = datetime.datetime.utcnow()

            item.filename = item.download_attachment()
            item.save()
            
            yield item

class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    guid = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.filename
    
    def download_attachment(self):
        data = None
        filename = os.path.basename(self.url)
        destination = os.path.join(settings.TORRENT_DOWNLOAD_PATH, filename)
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