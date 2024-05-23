from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerial(serializers.Serializer):
    class Meta:
        model = User
        fields = ["id",  "first_name", "last_name", "username"]


class CategorySerial(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"


class OptionSerial(serializers.Serializer):
    class Meta:
        model = Option
        fields = "__all__"


class PollSerial(serializers.Serializer):
    options = OptionSerial(many=True)
    user = UserSerial(many=True)

    class Meta:
        model = Poll
        fields = "__all__"