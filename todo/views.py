from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError


def home(request):
    return render(request, 'todo/home.html')


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
