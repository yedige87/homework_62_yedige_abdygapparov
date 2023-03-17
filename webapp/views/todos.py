from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.utils.http import urlencode

from webapp.forms import ToDoForm, SearchForm, ProjectForm
from webapp.models import Project
from webapp.models.todos import ToDo


class ToDoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'todo_create.html'
    model = ToDo
    form_class = ToDoForm

    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})


class ToDoDetail(DetailView):
    template_name = 'todo.html'
    model = ToDo


class ToDoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'todo_update.html'
    form_class = ToDoForm
    model = ToDo

    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})


class ToDoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'todo_confirm_delete.html'
    model = ToDo
    success_url = reverse_lazy('index')

class ProjectTasksView(ListView):
    template_name = 'project_tasks.html'
    model = ToDo
    context_object_name = 'todos'
    ordering = ('created_at',)
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.project_id = kwargs['project_id']
        print('project_id =', self.project_id)
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.project_id:
            print('self.project_id =', self.project_id)
            query = Q(project=self.project_id)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('created_at',)

class ProjectCreateView(CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('projects_view')


class ProjectToDoCreateView(CreateView):
    initial = {'project_id': '1'}
    template_name = 'project_todo_create.html'
    model = ToDo
    form_class = ToDoForm

    def get(self, request, *args, **kwargs):
        print('request = ', request)
        print('args = ', args)
        print('kwargs = ', kwargs)
        pk = kwargs['pk']
        print('pk = ', pk)
        args = (pk,)
        print('args = ', args)
        self.object = None
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('projects_view')