from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)


class Poll(models.Model):
    name = models.CharField(max_length=250)
    total_count = models.IntegerField(default=0, blank=True, null=True)
    user = models.ManyToManyField(User, blank=True)
    active = models.BooleanField(blank=True, null=True, default=False)
    # options = models.ManyToManyField('Option')


class Option(models.Model):
    name = models.CharField(max_length=250)
    count = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)










