from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import TaskForm, SearchForm, ProjectForm
from webapp.models import Task, Project


class ProjectListView(ListView):
    template_name = "projects/projects_list.html"
    model = Project
    context_object_name = "projects"
    # ordering = ("-created_at")
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
            queryset = queryset.filter(Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value))

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


class DetailProjectView(DetailView):
    template_name = 'projects/detail_project.html'
    model = Project
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object
        context['tasks'] = self.object.tasks.order_by('-created_at')
        context['search_form'] = SearchForm(self.request.GET)  # если нужна форма
        return context
#
class CreateProjectView(LoginRequiredMixin, CreateView):
    template_name = 'projects/create_project.html'
    form_class = ProjectForm

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
#
class UpdateProjectView(UpdateView):
    #
    template_name = 'projects/update_project.html'
    form_class = ProjectForm
    model = Project

#PermissionRequiredMixin,

    # permission_required = 'tasks.change_task'
    #
    # def has_permission(self):
    #     return super().has_permission() and self.request.user == self.get_object().author
#
#
#
#         # def dispatch(self, request, *args, **kwargs):
#     #     user = self.request.user
#     #     if not user.is_authenticated:
#     #         return redirect('webapp:login')
#     #     elif not user.has_perm('tasks.change_task') and user != self.get_object().author:
#     #         raise PermissionDenied
#     #     return super().dispatch(request, *args, **kwargs)
#
#
class DeleteProjectView(DeleteView):
    template_name = "projects/delete_project.html"
    # model = Task
    queryset = Project.objects.all()
    success_url = reverse_lazy('webapp:projects_list')
#
#PermissionRequiredMixin,
#     permission_required = 'tasks.delete_task'
#
#     def has_permission(self):
#         return super().has_permission() and self.request.user == self.get_object().author
#
# class DeleteAllTasksView(LoginRequiredMixin, View):
#     def post(self, request, *args, **kwargs):
#         ids = request.POST.getlist('task_ids')
#         if ids:
#             Task.objects.filter(id__in=ids).delete()
#         return redirect('webapp:index')





