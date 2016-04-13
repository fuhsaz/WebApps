from django.contrib import admin

# Register your models here.
from .models import Puzzle

class PuzzleAdmin(admin.ModelAdmin):
	list_display = 'id', 'difficulty', 'number_easy', 'number_medium', 'number_hard'

admin.site.register(Puzzle, PuzzleAdmin)