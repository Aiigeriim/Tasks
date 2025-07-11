from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.order_by('-created_at')
        return context


class CreateTaskView(View):

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.type.set(form.cleaned_data['type'])
            return redirect('detail_task', pk=task.pk)
        else:
            return render(request, 'create_task.html', {'form': form})

    def get(self, request):
        form = TaskForm()
        return render(request, 'create_task.html', {"form": form})


class DeleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')

    def get(self, request, pk):
        return render(request, 'delete_task.html', {'pk': pk})


class UpdateTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            task.types.set(form.cleaned_data['type'])
            return redirect('detail_task', pk=task.pk)
        else:
            return render(request, 'update_task.html', {'form': form})


    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'update_task.html', {'form': form})

class DetailTaskView(TemplateView):
    # template_name = 'detail_task.html'

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_template_names(self):
        if self.task.status:
            return ['detail_task.html']
        else:
            return ['detail_task.html']

def delete_all_tasks(request):
    ids = request.POST.getlist('task_ids')
    if ids:
        Task.objects.filter(id__in=ids).delete()
    return redirect('index')



