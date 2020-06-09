from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    mobile = models.CharField(max_length=20, blank=False, default='')
    subject = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=500, blank=False, default='')
