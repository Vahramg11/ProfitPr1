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

    class Meta:
        model = Poll
        fields = "__all__"

class PollOptionSerial(serializers.Serializer):
    options = OptionSerial(many=True)
    name = serializers.CharField()
    total_count = serializers.IntegerField(default=0)
    active=serializers.BooleanField(default=False)
    category=serializers.IntegerField()


    def create(self, validated_data):
        options_data = validated_data.pop('options')
        print("hello", validated_data)
        category = Category.objects.get(id=1)
        print("categ", category)
        validated_data = {**validated_data, "category": category}
        poll = Poll.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(**option_data)

        return poll



