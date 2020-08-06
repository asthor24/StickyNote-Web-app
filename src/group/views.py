from django.http import HttpResponse
from django.shortcuts import render
from .forms import GroupModelForm, Group
from .models import Membership
from django.contrib.auth.decorators import login_required
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
