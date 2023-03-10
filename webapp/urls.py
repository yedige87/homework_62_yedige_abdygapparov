from django.urls import path

from webapp.views.base import IndexView
from webapp.views.todos import ToDoCreateView, ToDoDetail, ToDoUpdateView, ToDoDeleteView, ProjectTasksView, \
    ProjectsView, ProjectCreateView, ProjectToDoCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name='index'),
    path('todo/add/', ToDoCreateView.as_view(), name='todo_add'),
    path('todo/<int:pk>', ToDoDetail.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update/', ToDoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', ToDoDeleteView.as_view(), name='todo_delete'),
    path('todo/<int:pk>/confirm_delete/', ToDoDeleteView.as_view(), name='confirm_delete'),
    path('project/<int:project_id>', ProjectTasksView.as_view(), name='project_detail'),
    path('projects/', ProjectsView.as_view(), name='projects_view'),
    path('project/add', ProjectCreateView.as_view(), name='project_add'),
    path('project/add/<int:pk>', ProjectToDoCreateView.as_view(), name='todo_project_add'),
    ]
