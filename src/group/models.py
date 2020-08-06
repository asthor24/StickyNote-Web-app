from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(User, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
