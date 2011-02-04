from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

class FeedItem(models.Model):
	feed = models.ForeignKey(Feed)
	title = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	filename = models.CharField(max_length=255)
