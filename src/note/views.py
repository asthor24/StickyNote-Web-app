from django.shortcuts import render
from .forms import StickyNoteForm, StickyNoteModelForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

from .models import StickyNote
def sticky_note_detail_page(request, note_id):
    obj = StickyNote.objects.get(id = note_id)
    template_name = "sticky_note_detail.html"
    context = {"object" : obj}
    return render(request, template_name, context)

def sticky_note_overview_page(request):
    objs = StickyNote.objects.all()
    template_name = "sticky_note_overview.html"
    context = {"objects" : objs}
    return render(request, template_name, context)

def sticky_note_test_page(request):
    objs = StickyNote.objects.all()
    template_name = "sticky_note.html"
    context = {"objects" : objs}
    return render(request, template_name, context)

@login_required
def sticky_note_create_page(request):
    print(request.user)
    form = StickyNoteModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StickyNoteModelForm()
    template_name = "sticky_note_create.html"
    context = {"form":  form}
    return render(request, template_name, context)

@csrf_exempt
def update_count(request):
    if request.method == 'POST':
        print(request.POST.keys())
        print(request.POST["count"])
    return HttpResponse('bongo')