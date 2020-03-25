from django.contrib.auth import views, models, login, authenticate
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth


def signup(request):
    if request.method == "POST":  # 1
        form = UserForm(request.POST)
        if form.is_valid():  # 2
            new_user = models.User.objects.create_user(**form.cleaned_data)  # 5
            login(request, new_user)
            return redirect("main")

    else:  # 3
        form = UserForm()

    return render(request, "account/signup.html", {"form": form})  # 4


def llogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            return HttpResponse("로그인 실패. 다시 시도 해보세요.")
    else:
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect("main")
