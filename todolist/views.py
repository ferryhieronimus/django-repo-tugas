from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from todolist.models import ToDoList

from django.http import HttpResponse
from django.core import serializers

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_objects = sorted(ToDoList.objects.filter(user=request.user), key=lambda x: x.is_finished)
    context = {
        "todolist": todolist_objects, 
        "username": request.user, 
        'last_login': request.COOKIES['last_login'],}
    return render(request, "todolist.html", context)

data_todolist = ToDoList.objects.all()

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie(
                'last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/todolist/login/")
def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        ToDoList.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        )
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    return render(request, "create_todo.html")

@login_required(login_url="/todolist/login/")
def delete_todo(request, id):
    todo = ToDoList.objects.get(user=request.user, id=id)
    todo.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url="/todolist/login/")
def update_status(request, id):
    todo = ToDoList.objects.get(user=request.user, id=id)
    todo.is_finished = not todo.is_finished
    todo.save(update_fields=["is_finished"])
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def show_xml(request):
    data = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")