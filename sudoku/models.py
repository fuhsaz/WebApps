from django.db import models

# Create your models here.
class Puzzle(models.Model):
	contents = models.CharField(max_length=81)
	difficulty = models.CharField(max_length=7)
	difficultyAsNumber = models.IntegerField(default=0)
	number_easy = models.IntegerField(default=0)
	number_medium = models.IntegerField(default=0)
	number_hard = models.IntegerField(default=0)