# mynock
# Copyright (c) 2011 Phil Christensen
#
#
# See LICENSE for details

from django.contrib import admin
from mynock.shows.models import Show

class ShowAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Show, ShowAdmin)
