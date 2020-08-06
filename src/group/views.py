from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GroupModelForm, Group
from .models import Membership
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def groups_page(request):
    template_name = "groups.html"
    context = {"groups": Group.objects.all(), "user": request.user}
    return render(request, template_name, context)

@login_required
def group_create_page(request):
    form = GroupModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        meme = Membership(person = request.user, group = obj)
        meme.save()
        form = GroupModelForm()
    template_name = "group_create.html"
    context = {"form":  form}
    return render(request, template_name, context)

@csrf_exempt
def group_manage_page(request, group_name):
    if request.user not in Group.objects.get(name = group_name).members.all():
        return redirect("../")

    if request.method == "POST":
        option = request.POST["management_option"]
        user_name = request.POST["user_name"]
        print(request.POST)
        obj = Group.objects.get(name = group_name)
        if option.lower() == "add":
            if len(obj.members.get(username = user_name)) < 1:
                meme = Membership(person = User.objects.get(username = user_name), group = obj)
                meme.save()
        else:
            if obj.members.get(username = user_name):
                print("here")
                obj.members.remove((User.objects.get(username = user_name).id))
                obj.save()

    template_name = "group_manage.html"
    context = {}
    return render(request, template_name, context)
