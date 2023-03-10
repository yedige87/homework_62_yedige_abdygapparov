
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.utils.http import urlencode


from webapp.forms import ToDoForm, SearchForm

from webapp.models.todos import ToDo


class ToDoCreateView(CreateView):
    template_name = 'todo_create.html'
    model = ToDo
    form_class = ToDoForm

    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})


class ToDoDetail(DetailView):
    template_name = 'todo.html'
    model = ToDo


class ToDoUpdateView(UpdateView):
    template_name = 'todo_update.html'
    form_class = ToDoForm
    model = ToDo

    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})


class ToDoDeleteView(DeleteView):
    template_name = 'todo_confirm_delete.html'
    model = ToDo
    success_url = reverse_lazy('index')
