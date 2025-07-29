# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
#
#
# def login_view(request):
#     context = {}
#     if request.method == 'POST':
#         print("post", request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         next_param = request.POST.get('next', 'webapp:index')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(next_param)
#         else:
#             context['has_error'] = True
#
#     context['next_param'] = request.GET.get('next')
#     return render(request, 'login.html', context=context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('webapp:index')
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import MyUserCreationForm

User = get_user_model()

class RegisterView(CreateView):
    template_name = 'user_create.html'
    model = User
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')

        if not next_page:
            next_page = reverse('webapp:index')

        return next_page

