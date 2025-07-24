from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import FormView, ListView, DetailView, CreateView
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

class CreateTaskView(CreateView):
    template_name = 'tasks/create_task.html'
    form_class = TaskForm



    # def get_success_url(self):
    #     return reverse('detail_task', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     task = form.save()
    #     return  redirect('detail_task', pk=task.pk)


class UpdateTaskView(FormView):
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
        return redirect('detail_task', pk=self.task.pk)

class DeleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')

    def get(self, request, pk):
        return render(request, 'tasks/delete_task.html', {'pk': pk})


class DetailTaskView(DetailView):
    template_name = 'tasks/detail_task.html'
    model = Task
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['types'] = self.object.type.order_by('-created_at')
        return result

def delete_all_tasks(request):
    ids = request.POST.getlist('task_ids')
    if ids:
        Task.objects.filter(id__in=ids).delete()
    return redirect('index')



