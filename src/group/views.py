from django.http import HttpResponse
from django.shortcuts import render
from .forms import GroupModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def groups_page(request):
    return render(request, "groups.html", {})

@login_required
def group_create_page(request):
    form = GroupModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = GroupModelForm()
    template_name = "group_create.html"
    context = {"form":  form}
    return render(request, template_name, context)