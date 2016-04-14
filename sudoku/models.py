from django.db import models
from django.contrib.auth.models import User

# The puzzles
class Puzzle(models.Model):
	id = models.AutoField(primary_key=True)
	contents = models.CharField(max_length=81)
	difficulty = models.CharField(max_length=7)
	difficultyAsNumber = models.IntegerField(default=0)
	number_easy = models.IntegerField(default=0)
	number_medium = models.IntegerField(default=0)
	number_hard = models.IntegerField(default=0)

	def __str__(self):
		return str(self.id)

	def as_dict(self):
		return {"id":self.id,"difficulty":self.difficulty}

	class Meta:
		ordering = ['difficultyAsNumber','number_hard','number_medium','number_easy']


# Puzzles each user has had
class User_Puzzle(models.Model):
	user = models.ForeignKey(User)
	puzzle = models.ForeignKey(Puzzle)
	

