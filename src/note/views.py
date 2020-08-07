from django.shortcuts import render , get_object_or_404 , redirect
from .forms import StickyNoteForm, StickyNoteModelForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import ValidationError
#from .serializers import UserSerializers, GroupSerializers
# Create your views here.

from .models import StickyNote
def sticky_note_detail_page(request, note_id):
    obj = StickyNote.objects.get(id = note_id)
    if obj.user != request.user:
        #raise ValidationError("You are not the author of this note")
        return redirect("../")
    else:
        template_name = "sticky_note_detail.html"
        context = {"object" : obj}
        return render(request, template_name, context)

def sticky_note_overview_page(request):
    objs = StickyNote.objects.filter(user = request.user)
    print(request.user)
    template_name = "sticky_note_overview.html"
    context = {"objects" : objs}
    print(context)
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
        objs = StickyNote.objects.all()
        posdict = dict(request.POST)
        #print(type(posdict), posdict)
        for note in objs:
            if len(posdict[str(note.id) + '[]']) == 0:
                continue
            #print(posdict[str(note.id) + '[]'])
            X, Y = posdict[str(note.id) + '[]'] if posdict[str(note.id) + '[]'] else (None, None)
            if (not X) or (not Y):
                continue
            xScreen, yScreen = map(int, (posdict["xScreen"][0], posdict["yScreen"][0]))
            note.x = int(int(float(X.replace("px", "")))*100/xScreen)
            note.y = int(int(float(Y.replace("px", "")))*100/yScreen)
            note.save()
    return HttpResponse('Hue')

@csrf_exempt
def ajax_note_update_content_page(request):
    if request.method == "POST" and request.is_ajax():
        contentdict = dict(request.POST)
        note = StickyNote.objects.get(id=int(contentdict["id"][0]));
        header = contentdict["header"][0]
        content = contentdict["content"][0]
        
        #note = list(objs[0])
        note.title = header
        note.content = content
        note.save()
    return HttpResponse('Hue')

@csrf_exempt
def ajax_note_update_zindex_page(request):
    if request.method == "POST" and request.is_ajax():
        contentdict = dict(request.POST)
        this_note = StickyNote.objects.get(id=contentdict["id"][0]);
        this_zindex = int(contentdict["zindex"][0])
        print("NEW Z-INDEX:",this_zindex)
        print("OLD Z-INDEX:",this_note.zindex)
        print("This note:", repr(this_note))
        #print(dir(this_note))
        this_note.zindex = this_zindex
        this_note.save()
        this_note.zindex = this_zindex
        this_note.save()
    return HttpResponse('Hue')