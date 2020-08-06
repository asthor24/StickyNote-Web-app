from django import forms
from .models import StickyNote
class StickyNoteForm(forms.Form):
    title = forms.CharField()
    content =  forms.CharField()
    x = 0
    y = 0
    slug = ""

class StickyNoteModelForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ['title', 'content']

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 200:
            raise forms.ValidationError("Ma dude be more concise")
        return content
