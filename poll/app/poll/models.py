from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)


class Poll(models.Model):
    name = models.CharField(max_length=250)
    total_count = models.IntegerField(default=0, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="polls")




class Option(models.Model):
    name = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    count = models.IntegerField(default=0)








