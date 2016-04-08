from django.db import models

# Create your models here.
class Puzzle(models.Model):
	contents = models.CharField(max_length=81)
	difficulty = models.CharField(max_length=7)