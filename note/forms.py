from django import forms
from .models import StickyNote
class StickyNoteForm(forms.Form):
    title = forms.CharField()
    content =  forms.CharField()
    x = 0
    y = 0
    zindex = 0
    slug = ""

class StickyNoteModelForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ['title', 'content']

    def clean_content(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        qs = StickyNote.objects.filter(title__iexact = title )
        if instance is not None:
            qs = qs.exclude(pk = instance.pk)
        content = self.cleaned_data.get('content')
        if len(content) > 200:
            raise forms.ValidationError("Ma dude be more concise")
        return content
