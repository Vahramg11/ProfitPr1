from django.contrib import admin

from .models import Category, Poll, Option

admin.site.register(Category),
admin.site.register(Poll),
admin.site.register(Option)
