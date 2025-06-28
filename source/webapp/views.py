

from django.http import HttpResponseRedirect
# Create your views here.

from django.shortcuts import render
from .cat import Cat

current_cat = None

def create_name(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            current_cat = Cat(name=name)
            print(current_cat)
        return HttpResponseRedirect("/")
    else:
        return render(request, 'create_cat.html')

def cat_view(request):

    create_name(request)
    name = request.GET.get('name')
    cat = Cat(name=name)
    message = ""
    if request.method == "POST":
        action = request.POST.get('cat_action')

        if action == "play":
            message = cat.play()
        elif action == "feed":
            message = cat.eat()
        elif action == "sleep":
            message = cat.sleep()

        cat.cat_avatar = cat.set_new_avatar()
    return render(request, 'index.html', {'cat': cat, 'message': message})






