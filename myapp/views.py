from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from myapp.models import *


def projects(request):  
   # Datu-baseko proiektu guztiak lortu
   projects_list = Project.objects.all()
   # Txantiloiari datuak pasatu 'projects' izeneko aldagai batean
   return render(request, 'projects.html', {
       'projects': projects_list
   })

def atazak_todo(request):  
    
   task_list = Task.objects.filter(done=False)
   return render(request, 'tasks.html', {
       'tasks': task_list
   })

def proiektuaren_atazak(request, project_id):  
   
   task_list = Task.objects.filter(project_id=project_id)
   return render(request, 'tasks.html', {
       'tasks': task_list
   })
   

def mark_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = True
    task.save()
    return redirect(f'/projects/{task.project.id}/tasks/')


def mark_task_undone(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = False
    task.save()
    return redirect(f'/projects/{task.project.id}/tasks/')

   
class ProiektuaCreateView(CreateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['name']
    success_url = reverse_lazy('projects')

class ProiektuaUpdateView(UpdateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['name']
    success_url = reverse_lazy('projects')

class ProiektuaDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('projects')
    
    
class AtazaCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'project']  # Sortzerakoan done kendu
    success_url = reverse_lazy('tasks_todo')

class AtazaUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'project', 'done']
    success_url = reverse_lazy('tasks_todo')

class AtazaDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('tasks_todo')