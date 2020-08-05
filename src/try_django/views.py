from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    mytitle = "what nana"
    return render(request, "home_page.html", {"title": repr(request)})

def about_page(request):
    return render(request, "about.html", {"title": "about this page"})
