from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm, SearchForm
from webapp.models import Task

class TaskListView(ListView):
    template_name = "projects/projects_list.html"
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateTaskView(PermissionRequiredMixin, UpdateView):
    template_name = 'tasks/update_task.html'
    form_class = TaskForm
    model = Task

    permission_required = 'tasks.change_task'

    def has_permission(self):
        return super().has_permission() and self.request.user == self.get_object().author



        # def dispatch(self, request, *args, **kwargs):
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return redirect('webapp:login')
    #     elif not user.has_perm('tasks.change_task') and user != self.get_object().author:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class DeleteTaskView(PermissionRequiredMixin, DeleteView):
    template_name = "tasks/delete_task.html"
    # model = Task
    queryset = Task.objects.all()
    success_url = reverse_lazy('webapp:index')


    permission_required = 'tasks.delete_task'

    def has_permission(self):
        return super().has_permission() and self.request.user == self.get_object().author

class DetailTaskView(DetailView):
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





