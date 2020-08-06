from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth import authenticate, login

def user_creation_page(request):
    form = UserCreateForm(request.POST or None)
    template_name = "user_creation.html"
    context = {"form": form}
    if form.is_valid():
        print(form.is_valid())
        obj = form.save(commit=False)
        obj.save()
    return render(request, template_name , context)

def login_page(request):
    form = UserLoginForm(request.POST or None)
    context = {"form":form}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("../note/")

    return render(request, "login.html", context)
