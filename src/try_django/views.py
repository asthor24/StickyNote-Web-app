from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    mytitle = "what nana"
    return render(request, "home_page.html", {"title": repr(request)})

def about_page(request):
    return render(request, "about.html", {"title": "about this page"})

def form_page(request):
    form = ContactForm(request.POST or None)
    #do stuff wiht form
    if form.is_valid():
        form = ContactForm()
    context  ={
                "form" : form
    }
    return render(request, "form.html",context)

def groups_page(request):
    return render(request, "groups.html", {})