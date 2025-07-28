from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm, SearchForm
from webapp.models import Task

class TaskListView(ListView):
    template_name = "tasks/index.html"
    model = Task
    context_object_name = "tasks"
    ordering = ("-created_at")
    paginate_by = 5
    paginated_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(summary__icontains=self.search_value) | Q(status__name__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list = None, **kwargs):
        result = super().get_context_data(**kwargs)
        result['search_form'] = self.form
        if self.search_value:
            result['query'] = urlencode({'search': self.search_value})
            result['search'] = self.search_value
        return result

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]

class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create_task.html'
    form_class = TaskForm


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/update_task.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['task'] = self.task
        return context

    def form_valid(self, form):
        form.save()
        return redirect('webapp:detail_task', pk=self.task.pk)

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    template_name = "tasks/delete_task.html"
    # model = Task
    queryset = Task.objects.all()
    success_url = reverse_lazy('webapp:index')

class DetailTaskView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/detail_task.html'
    model = Task
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['types'] = self.object.type.order_by('-created_at')
        return result


class DeleteAllTasksView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        ids = request.POST.getlist('task_ids')
        if ids:
            Task.objects.filter(id__in=ids).delete()
        return redirect('webapp:index')





