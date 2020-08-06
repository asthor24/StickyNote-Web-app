from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL
class StickyNote(models.Model):
    user = models.ForeignKey(User, default = 1, null = True, on_delete= models.SET_NULL)
    title = models.CharField(max_length =120)
    x = models.IntegerField(blank = True, null = True)
    y = models.IntegerField(blank = True, null = True)
    slug = models.SlugField(blank = True, null = True)
    content = models.TextField(null= True, blank = True)

    def update_position(self, X,Y):
        self.x = X
        self.y = Y
        return
