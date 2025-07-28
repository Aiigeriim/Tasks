from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    context = {}
    if request.method == 'POST':
        print("post", request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_param = request.POST.get('next', 'webapp:index')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_param)
        else:
            context['has_error'] = True

    context['next_param'] = request.GET.get('next')
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:index')