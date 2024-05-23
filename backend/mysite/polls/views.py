from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .forms import Sign_Up_Form, PollForm, OptionForm
from .models import Option, Poll
from .serializers import PollSerial


@api_view(['POST'])
def sign_up(request):
    user_form = Sign_Up_Form(request.data)
    print(request.data)
    if user_form.is_valid():
        user_form.save()
        return Response({"message": "Success"}, status=status.HTTP_200_OK)
    else:
        return Response({"errors": user_form.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def sign_in(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'message': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"massage": "invalid info"}, status=status.HTTP_401_UNAUTHORIZED)
    # return Response({'token': "ok"}, status=status.HTTP_200_OK)

    else:
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_poll(request):
    data = PollForm(request.data)
    if data.is_valid():
        poll = data.save()
        options_data = request.data.get("options", [])
        for option_data in options_data:
            option_data["poll"] = poll.id
            option_form = OptionForm(option_data)
            if option_form.is_valid():
                option_form.save()
            else:
                return Response(option_form.errors, status=400)
        return Response("Poll added successfully", status=201)
    else:
        return Response(data.errors, status=400)


@api_view(["PATCH"])
def activate(request, pk):
    opt = Poll.objects.get(id=pk)
    opt.active = not opt.active
    opt.save()
    serial = PollSerial(opt)
    return Response(serial.data)


@api_view(["GET"])
def all_polls(request):
    polls = Poll.objects.all()
    serial = PollSerial(polls, many=True)
    return Response(serial.data)


#
# "
# {
# "username": "Poxos123",
# "password": "pp123pp."
# }
# "


# {
# "first_name":"Poxos",
# "last_name":"Poxosyan",
# "username":"Poxos123",
# "password1":"pp123pp.",
# "password2":"pp123pp.",
# }




# {
# "name": "How are you",
# "total_count":  4,
# "user": "Poxos"
# }






