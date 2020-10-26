from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from .models import Todo

# todos&others


def home(request):
    return render(request, 'todo/home.html')


def todos(request):
    current = Todo.objects.filter(
        user=request.user, completeDate__isnull=True)
    done = Todo.objects.filter(user=request.user, completeDate__isnull=False)
    return render(request, 'todo/todos.html', {'current': current, 'done': done})


def detail(request, todoId):
    todo = get_object_or_404(Todo, pk=todoId)
    return render(request, 'todo/detail.html', {'todo': todo})

# auth


def sign(request):
    if request.method == 'GET':
        return render(request, 'todo/sign.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], "", request.POST['password1'])
            except IntegrityError:
                error = "This username is already taken. Try different one."
                return render(request, 'todo/sign.html',
                              {'error': error, 'form': UserCreationForm()})
            else:
                user.save()
                login(request, user)
                return redirect(home)
        else:
            error = "Passwords didn't match. Try again."
            return render(request, 'todo/sign.html',
                          {'error': error, 'form': UserCreationForm()})


def log(request):
    if request.method == 'GET':
        return render(request, 'todo/log.html',
                      {'form': AuthenticationForm()})
    else:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Username or password is incorrect. Try again."
            return render(request, 'todo/log.html',
                          {'form': AuthenticationForm(), 'error': error})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
