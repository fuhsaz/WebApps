from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout, views
from random import randint
from .models import Puzzle
import json
# Home page
def index(request):
	return render(request, 'sudoku/index.html')

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
	        login(request, user)
	        # Redirect to a success page.
	        return render(request, 'sudoku/index.html')
	else:
	    # Return an 'invalid login' error message.
	    return render(request, 'sudoku/login_view.html')

def logout(request):
	logout(request)
	return render(request, 'sudoku/index.html')

# Page where the user can pick a puzzle based on difficulty and other factors
def pick(request):
	puzzle_list = Puzzle.objects.all()
	return render(request, 'sudoku/pick.html', {'puzzle_list':puzzle_list})

# Display a preview of a puzzle
def preview(request):
	puzzleID = request.POST['id']
# If id is left at 0, selects a random puzzle. Otherwise, selects the puzzle with the given id
def puzzle(request, id):
	if id == '0':
		maxInd = Puzzle.objects.filter().count()
		minInd = 1
		randInd = randint(minInd, maxInd)
		puzzle = get_object_or_404(Puzzle, pk=randInd)
	else:
		puzzle = get_object_or_404(Puzzle, pk=id)
	contents = puzzle.contents
	contentsList = []
	for s in contents:
		if s != '0':
			contentsList.append(s)
		else:
			contentsList.append(" ")
	return render(request, 'sudoku/puzzle.html', {'puzzle':puzzle, 'contentsList':contentsList})

def filterPuzzles(request):
	diff = request.POST['difficulty']
	if diff == 'all':
		puzzle_list = Puzzle.objects.all()
	else:
		puzzle_list = Puzzle.objects.filter(difficulty=diff)
	if request.is_ajax():
		puzzles = [ puzzle.as_dict() for puzzle in puzzle_list ]
	return HttpResponse(json.dumps({"data": puzzles}), content_type='application/json')











	