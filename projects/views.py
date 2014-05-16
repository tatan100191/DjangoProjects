from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from projects.models import Project, Task
import time


# Create your views here.
def projectsInProgress(request):
    projects = Project.objects.all() 
    project_list = []
    for project in projects:
    	if not project.completed:
    		project_list.append(project)
    return render(request, 'projectsProgress.html', {'project_list': project_list})

def projectsCompleted(request):
    projects = Project.objects.all() 
    project_list = []
    for project in projects:
    	if  project.completed:
    		project_list.append(project)
    return render(request, 'projectsCompleted.html', {'project_list': project_list})

def addProject(request):
	project = Project(name=request.POST["addproject"])
	project.save()
	return HttpResponseRedirect(reverse('projects:projectsInProgress'))

def taskCompleted(request, project_id, task_id):
	task = get_object_or_404(Task, id=task_id)
	task.end_date = datetime.date.today()
	task.save()
	return HttpResponseRedirect(reverse('projects:tasks', args=(project_id,)))

def projectCompleted(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	project.end_date = datetime.date.today()
	project.completed = True
	project.save()
	return HttpResponseRedirect(reverse('projects:projectsInProgress'))

def tasks(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'tasks.html', {'project': project, 'tasks':tasks})

def addTask(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	project.task_set.create(name=request.POST["addtask"])
	return HttpResponseRedirect(reverse('projects:tasks', args=(project_id,)))

def start(request, project_id, task_id):
	global start
	start = time.time()
	return HttpResponseRedirect(reverse('projects:tasks', args=(project_id,)))

def pause(request, project_id, task_id):
	task = get_object_or_404(Task, id=task_id)
	time_f =  time.time() 
	time_int = int(time_f -  start)
	minutes = time_int/60
	task.hours_worked = task.hours_worked + minutes
	task.save()
	return HttpResponseRedirect(reverse('projects:tasks', args=(project_id,)))