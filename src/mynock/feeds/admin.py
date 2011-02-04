from django.contrib import admin
from mynock.feeds.models import Feed, FeedItem

class FeedAdmin(admin.ModelAdmin):
	list_display = ('name', 'url')

class FeedItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedItem, FeedItemAdmin)