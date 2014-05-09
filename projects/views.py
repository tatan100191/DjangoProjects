from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def projectsInProgress(request):
	return render_to_response('projectsInProgress.html')

def createProject(request):
	return render_to_response('createProject.html')

def addTask(request):
	return render_to_response('addTask.html')

def generateReceipt(request):
	return render_to_response('generateReceipt.html')

def projectsCompleted(request):
	return render_to_response('projectsCompleted.html')

def tasks(request):
	return render_to_response('tasks.html')