from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, status_choices


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('completion_date')
    return render(request, 'index.html', {"tasks": tasks} )


def create_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        completion_date = request.POST.get('mydate')
        task = Task.objects.create(name=name, description=description, status=status, completion_date=completion_date)
        return redirect('detail_task', pk=task.pk)
    else:
        return render(request, 'create_task.html', {"status_choices": status_choices})

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
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.completion_date = request.POST.get('mydate')
        task.save()
        return redirect('detail_task', pk=task.pk)
    else:
        context = {
            'task': task,
            'status_choices': status_choices,
        }
        return render(request, 'update_task.html', context)


def detail_task(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'detail_task.html', {"task": task})



