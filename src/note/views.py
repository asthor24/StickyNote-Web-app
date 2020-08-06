from django.shortcuts import render , get_object_or_404 , redirect
from .forms import StickyNoteForm, StickyNoteModelForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
#from .serializers import UserSerializers, GroupSerializers
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
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = StickyNoteModelForm()
    template_name = "sticky_note_create.html"
    context = {"form":  form}
    return render(request, template_name, context)

def sticky_note_update_page(request, note_id):
    obj = get_object_or_404(StickyNote, id=note_id)
    form = StickyNoteModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
    template_name = "sticky_note_update.html"
    context = {"form":form , "object" : obj}
    return render(request, template_name, context)

def sticky_note_delete_page(request,note_id):
    obj = get_object_or_404(StickyNote, id=note_id)
    form = StickyNoteModelForm(request.POST or None, instance = obj)
    template_name = "sticky_note_delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("../..")
    context = {"form":form , "object":obj}
    return render(request, template_name, context)

@csrf_exempt
def ajax_note_update_page(request):
    if request.method == "POST" and request.is_ajax():
        reqDict = dict(request.POST)
        # Remove list from values
        reqDict = {key : val[0] for (key,val) in reqDict.items()}
        obj = StickyNote.objects.get(id=reqDict["note_id"])
        x, y = reqDict["x"], reqDict["y"]
        if not x or not y:
                raise ValueError("The post position was not found!")
        obj.x = int(float(x))
        obj.y = int(float(y))
        obj.save()
    return HttpResponse('Perfect!')
