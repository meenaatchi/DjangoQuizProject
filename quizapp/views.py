from django.shortcuts import render
from django.http import HttpResponse
from quizapp.models import Newuser
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def pythonquiz(request):
    return render(request, 'pythonquiz.html')


def djangoquiz(request):
    return render(request, 'djangoquiz.html')


def end(request):
    return render(request, 'end.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Newuser(username=username, email=email, password=password).save()
        messages.success(request, 'Registration done Successfully')
        return render(request, 'index.html')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        try:
            userdetails = Newuser.objects.get(username=request.POST['username'], password=request.POST['password'])
            print("username", userdetails)
            request.session["username"] = userdetails.username
            return render(request, 'home.html')
        except Newuser.DoesNotExist as e:
            messages.success(request, 'Invalid Credentials')
    return render(request, 'index.html')


def logout():
    pass


def home():
    args = {'user': request.user}
    return render(request, 'home.html', args)
