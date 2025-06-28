from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.models import Task, status_choices


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-completion_date')
    return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        status = request.POST.get('status')
        Task.objects.create(name=name, status=status)
        return HttpResponseRedirect("/")
    else:
        return render(request, 'create_task.html', {"status_choices": status_choices})


def task_detail(request):
    task_id = request.GET.get('id')
    if task_id:
        try:
            task = Task.objects.get(id=task_id)
            return render(request, 'detail_task.html', {"task": task})
        except Task.DoesNotExist:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")