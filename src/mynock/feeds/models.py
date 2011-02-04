from django.db import models

class Feed(models.Model):
    name = models.CharField()
    url = models.CharField()

    def has_new_items(self):
    	return False

class FeedItem(models.Model):
	feed = models.ForeignKey(Feed)
	title = models.CharField()
	url = models.CharField()
	filename = models.CharField()
