# mynock
# Copyright (c) 2011 Phil Christensen
#
#
# See LICENSE for details

from django.contrib import admin
from mynock.feeds.models import Feed, FeedItem

class FeedItemInline(admin.TabularInline):
    model = FeedItem

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

    inlines = [
        FeedItemInline,
    ]

class FeedItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedItem, FeedItemAdmin)