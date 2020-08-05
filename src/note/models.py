from django.db import models

# Create your models here.
class StickyNote(models.Model):
    title = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()
    slug = models.SlugField()
    content = models.TextField(null= True, blank = True)
