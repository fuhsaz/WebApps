from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Puzzle

def index(request):
	return HttpResponse("Welcome to Sudoku!")

def puzzle(request, id):
	puzzle = get_object_or_404(Puzzle, pk=id)
	contents = puzzle.contents
	contentsList = []
	for s in contents:
		if s != '0':
			contentsList.append(s)
		else:
			contentsList.append(" ")
	return render(request, 'sudoku/puzzle.html', {'puzzle':puzzle, 'contentsList':contentsList})
