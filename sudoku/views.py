from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout, views
from random import randint
from .models import Puzzle
import json
# Home page
def index(request):
	return render(request, 'sudoku/index.html')

def filterPuzzles(request):
	diff = request.POST['difficulty']
	if diff == 'all':
		puzzle_list = Puzzle.objects.all()
	else:
		puzzle_list = Puzzle.objects.filter(difficulty=diff)
	if request.is_ajax():
		puzzles = [ puzzle.as_dict() for puzzle in puzzle_list ]
	return HttpResponse(json.dumps({"data": puzzles}), content_type='application/json')

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
	puzzleID = int(request.POST['puzzleID'])
	puzzle = get_object_or_404(Puzzle, pk=puzzleID)
	contents = puzzle.contents
	counter = 1
	ret = "<table id='puzzle-preview'>"
	for each in contents:
		if counter%9 == 1:
			ret += "<tr>"
		ret += "<td class='cell ";

		# Adding the classes for thicker borders depending on where a cell is, in order to make the 3x3
		# Boxes stand out more
		if 1 <= counter and counter <= 9:
			ret += 'cell-top ';
		if 73 <= counter and counter <= 81:
			ret += 'cell-bottom ';
		if 19 <= counter and counter <= 27:
			ret += 'cell-bottom ';
		if 28 <= counter and counter <= 36:
			ret += 'cell-top ';
		if 46 <= counter and counter <= 54:
			ret += 'cell-bottom ';
		if 55 <= counter and counter <= 63:
			ret += 'cell-top ';
		if counter % 9 == 1 or counter % 9 == 4 or counter % 9 == 7:
			ret += 'cell-left ';
		if counter % 9 == 3 or counter % 9 == 6 or counter % 9 == 0:
			ret += 'cell-right ';
		
		ret += "'>";
		if each == '0':
			ret += ' '
		else: 
			ret += each
		ret += "</td>"
		if counter%9 == 0:
			ret += "</tr>"
		counter += 1
	ret += "</table>"

	return HttpResponse(json.dumps({"data": ret}), content_type='application/json')

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

# Function to save a user's progress when they click the save button
# Will check if they already have a saved version of that puzzle, and if so, delete it
def save(request):
	pass












	