# mynock
# Copyright (c) 2011 Phil Christensen
#
#
# See LICENSE for details

from django.db import models

class Show(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	
	def __str__(self):
		return self.name
