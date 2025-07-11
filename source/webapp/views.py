# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.views.generic import TemplateView, DetailView
#
# from webapp.forms import TaskForm
# from webapp.models import Task, status_choices
#
#
# class IndexView(View):
#
#     def get(self, request):
#         tasks = Task.objects.order_by('-created_at')
#         return render(request, 'index.html', {'tasks': tasks})
#
#
# class CreateTaskView(TemplateView):
#
#     def post(self,request):
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             tags = form.cleaned_data['tags']
#             task = form.save()
#             task.tags.set(tags)
#             return redirect('detail_task', pk=task.pk)
#         else:
#             return render(request, 'create_task.html', {'form': form})
#
#     def get(self, request):
#         form = TaskForm()
#         return render(request, 'create_task.html', {"form": form})
#
# def delete_task(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == "POST":
#         task.delete()
#         return redirect('index')
#     else:
#         context = {
#             'task': task,
#             'status_choices': status_choices,
#         }
#         return render(request, 'delete_task.html', context)
#
# def update_task(request, *args, pk, **kwargs):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             task = form.save()
#             task.tags.set(form.cleaned_data['tags'])
#             return redirect('detail_task', pk=task.pk)
#         else:
#             return render(request, 'update_task.html', {'form': form})
#     else:
#         form = TaskForm(instance=task, initial={'tags': task.tags.all})
#         return render(request, 'update_task.html', {'form': form})
#
#
#
# class DetailTaskView(TemplateView):
#     # template_name = 'detail_task.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         self.task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task'] = self.task
#         return context
#
#     def get_template_names(self):
#         if self.task.status == "new":
#             return ['detail_task.html']
#         else:
#             return ['detail_task.html']
#
# def delete_all_tasks(request):
#     ids = request.POST.getlist('task_ids')
#     if ids:
#         Task.objects.filter(id__in=ids).delete()
#     return redirect('index')
#
#
#
