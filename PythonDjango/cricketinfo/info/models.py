from django.db import models

# Create your models here.
class Country(models.Model):
	name = models.CharField(max_length = 250, unique=True)
	flag = models.ImageField(blank=True)
	shortname = models.CharField(max_length=250, unique=True)
	description = models.TextField(max_length=500,blank=True, null=True)
