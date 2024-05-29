from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .forms import Sign_Up_Form
from .models import Option, Poll
from .serializers import PollSerial, UserSerial, PollOptionSerial


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


# @api_view(["POST"])
# def add_poll(request):
#     data = request.data
#     polls = PollSerial(data=request.data)
#     if polls.is_valid():
#         user = UserSerial(data =data["user"])
#         print(user.is_valid())
#         print(data["options"])

    # if data.is_valid():
    #     data.save()
    #     options_data = request.data.get("options")
    #     for option_data in options_data:
    #         option_form = OptionSerial(data=option_data)
    #         if option_form.is_valid():
    #             option_form.save()
    #         else:
    #             return Response(option_form.errors, status=400)
    #     return Response("Poll added successfully", status=201)
    # else:
    #     return Response(data.errors, status=400)

@api_view(['POST'])
def add_poll(request):
    print(request.data)
    serializer = PollOptionSerial(data = request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        print(serializer.save())
        return Response("data", status=status.HTTP_201_CREATED)
    return Response("serializer.errors", status=status.HTTP_400_BAD_REQUEST)


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
    print(serial.data)
    return Response(serial.data)


@api_view(['GET'])
def get_active_polls(request):
    active_polls = Poll.objects.filter(active=True)
    serializer = PollSerial(active_polls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerial(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# sign_in
# "
# {
# "username": "Poxos123",
# "password": "pp123pp."
# }
# "

# sign_up
# {
# "first_name":"Poxos",
# "last_name":"Poxosyan",
# "username":"Poxos123",
# "password1":"pp123pp.",
# "password2":"pp123pp.",
# }



# added
# {
#     "name": "Favorite Programming Language",
#     "active": true,
#     "category":1,
#     "options": [
#         {"name": "Python", "poll": 1},
#         {"name": "JavaScript", "poll": 1}
#     ]
# }
