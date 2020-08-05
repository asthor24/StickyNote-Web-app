from django.shortcuts import render

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
