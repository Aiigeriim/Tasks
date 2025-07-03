from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.order_by('completion_date')
    return render(request, 'index.html', {"tasks": tasks} )


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            completion_date = form.cleaned_data.get('completion_date')
            task = Task.objects.create(name=name, description=description, status=status, completion_date=completion_date)
            return redirect('detail_task', pk=task.pk)
        else:
            return render(request, 'create_task.html', {'form': form})

    else:
        form = TaskForm()
        return render(request, 'create_task.html', {"form": form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('index')
    else:
        context = {
            'task': task,
            'status_choices': status_choices,
        }
        return render(request, 'delete_task.html', context)

def update_task(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task.name = form.cleaned_data.get('name')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.completion_date = form.cleaned_data.get('completion_date')
            task.save()
            return redirect('detail_task', pk=task.pk)
        else:
            return render(request, 'update_task.html', {'form': form})
    else:
        form = TaskForm(initial={'name': task.name, 'description': task.description, 'status': task.status, 'completion_date': task.completion_date})
        return render(request, 'update_task.html', {'form': form})


def detail_task(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'detail_task.html', {"task": task})


def delete_all_tasks(request):
    ids = request.POST.getlist('task_ids')
    if ids:
        Task.objects.filter(id__in=ids).delete()
    return redirect('index')



