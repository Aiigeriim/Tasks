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
        completion_date = request.POST.get('myDate')

        task = Task.objects.create(name=name, description=description, status=status, completion_date=completion_date)
        return redirect('task_detail', pk=task.pk)
    else:
        return render(request, 'create_task.html', {"status_choices": status_choices})



def task_detail(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'detail_task.html', {"task": task})



