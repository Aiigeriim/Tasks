from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.order_by('-created_at')
        return context


class CreateTaskView(FormView):
    template_name = 'create_task.html'
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save()
        return  redirect('detail_task', pk=task.pk)


class UpdateTaskView(FormView):
    template_name = 'update_task.html'
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
        return render(request, 'delete_task.html', {'pk': pk})



class DetailTaskView(TemplateView):
    template_name = 'detail_task.html'

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

def delete_all_tasks(request):
    ids = request.POST.getlist('task_ids')
    if ids:
        Task.objects.filter(id__in=ids).delete()
    return redirect('index')



