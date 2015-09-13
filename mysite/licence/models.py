import datetime

from django.db import models
#from django.utils import timezone
# Create your models here.

class licence_model(models.Model):
	licence_number = models.CharField(max_length=30)
	scan_time = models.CharField(max_length=20)
	def __unicode__(self):
		return '%s %s' % (self.licence_number, self.scan_time)
		#return self.scan_time
		#return self.licence_number
		#return self.scan_time