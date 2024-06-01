from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Option, Poll


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]


class CategorySerial(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class OptionSerial(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class PollSerial(serializers.ModelSerializer):
    options = OptionSerial(many=True)
    used = serializers.BooleanField(allow_null=True)

    class Meta:
        model = Poll
        exclude = ["users"]


class PollOptionSerial(serializers.ModelSerializer):
    options = OptionSerial(many=True)

    class Meta:
        model = Poll
        fields = "__all__"

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        print(options_data)
        poll = Poll.objects.create(**validated_data)
        print(poll)
        for option_data in options_data:
            opt = Option.objects.create(**option_data, poll=poll)
            print(opt)
        return poll



