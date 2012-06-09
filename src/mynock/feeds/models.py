# mynock
# Copyright (c) 2011 Phil Christensen
#
#
# See LICENSE for details

import sys, os.path

from django.db import models
from django.conf import settings

from mynock.shows.models import Show 

import feedparser, urllib2, datetime

class Feed(models.Model):
	name = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	last_scan = models.DateTimeField(blank=True)
	show = models.ForeignKey(Show)
	
	def __str__(self):
		return self.url
	
	def get_new_items(self):
		self.last_scan = datetime.datetime.utcnow()
		self.save()
		
		parser = feedparser.parse(self.url)
		for entry in parser['items']:
			try:
				guid = entry.get('guid', entry['link'])
			except KeyError, e:
				raise KeyError("No GUID or LINK key in: %s" % entry)
			
			existing = FeedItem.objects.filter(feed=self, guid=guid)
			if(existing):
				continue
			
			item = FeedItem()
			item.feed = self
			item.guid = guid
			item.title = entry['title']
			item.url = entry['link']
			
			date_published = entry.get('published_parsed', entry.get('updated_parsed'))
			if date_published:
				item.pub_date = datetime.datetime(*date_published[:-3])
			else:
				item.pub_date = datetime.datetime.utcnow()
			
			try:
				item.filename = item.download_attachment()
			except Exception, e:
				print >>sys.stderr, "Couldn't download %s: %s" % (item.url, e)
			item.save()
			
			yield item

class FeedItem(models.Model):
	feed = models.ForeignKey(Feed)
	title = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	filename = models.CharField(max_length=255)
	guid = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	download_date = models.DateTimeField()
	
	def __str__(self):
		return self.filename
	
	def download_attachment(self):
		data = None
		from hashlib import md5
		self.filename = os.path.basename(self.url) or md5(self.url).hexdigest()
		destination = os.path.join(settings.TORRENT_DOWNLOAD_PATH, self.filename)
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
		self.download_date = datetime.datetime.now()
		return self.filename
