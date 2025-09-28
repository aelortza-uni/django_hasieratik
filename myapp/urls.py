from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='projects/')),
    path('projects/', views.projects, name='projects'),
    path('projects/create/', views.ProiektuaCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/edit/', views.ProiektuaUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.ProiektuaDeleteView.as_view(), name='project_delete'),    
    path('projects/<int:project_id>/tasks/', views.proiektuaren_atazak, name='project_tasks'),
    path('tasks/', views.atazak_todo, name='tasks_todo'),
    path('tasks/create/', views.AtazaCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/edit/', views.AtazaUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.AtazaDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:task_id>/done/', views.mark_task_done, name='task_done'),
    path('tasks/<int:task_id>/undone/', views.mark_task_undone, name='task_undone'),
]
