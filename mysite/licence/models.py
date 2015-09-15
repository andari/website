import datetime

from django.db import models
#from django.utils import timezone
# Create your models here.

class licence_model(models.Model):
	number = models.CharField(max_length=30)
	timestamp = models.CharField(max_length=20)
	def __unicode__(self):
		return '%s %s' % (self.number, self.timestamp)
		#return self.number
		#return self.timestamp
		#return self.scan_time