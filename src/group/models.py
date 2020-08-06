from django.db import models
from note.models import StickyNote
# Create your models here.
class Group(models.Model):
    note_ids = models.ManyToManyField(StickyNote)
    
