from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Poll(models.Model):
    name = models.CharField(max_length=250)
    total_count = models.IntegerField(default=0, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="polls", null=True)
    users = models.ManyToManyField(User, related_name="users", blank=True, null=True)

    def __str__(self):
        return self.name




class Option(models.Model):
    name = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options", blank=True)
    count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    # def vote(self):
    #     self.count += 1
    #     self.poll.total_count += 1
    #     self.save()
    #     self.poll.save()







