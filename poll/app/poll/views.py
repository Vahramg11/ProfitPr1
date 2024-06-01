from django.contrib.auth import authenticate, logout
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .forms import Sign_Up_Form
from .models import Option, Poll, Category
from .serializers import PollSerial, UserSerial, PollOptionSerial, CategorySerial, OptionSerial


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




# @permission_classes([IsAuthenticated, IsAdminUser])
@api_view(["POST"])
def add_poll(request):
    data = PollOptionSerial(data=request.data)
    print(data.is_valid())
    if data.is_valid():
        poll = data.save()
        new_data = PollSerial(poll)
        return Response(new_data.data, status=status.HTTP_200_OK)
    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

# {    "name": "Favorite Programming Language",
#     "total_count": 100,    "active": true,
#     "category": 1,    "options": [
#         {            "name": "Python"
#                     },
#         {            "name": "JavaScript"
#                  },
#         {            "name": "C++"
#                  }
#     ]}
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def activate(request, pk):
    opt = Poll.objects.get(id=pk)
    opt.active = not opt.active
    opt.save()
    serial = PollSerial(opt)
    return Response(serial.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def all_polls(request):
    polls = Poll.objects.annotate(
       used = Exists(
           Poll.users.through.objects.filter(
               poll_id=OuterRef('id'),
               user_id=request.user.id
           ))
    )
    serial = PollSerial(polls, many=True)
    print(serial.data)
    return Response(serial.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_active_polls(request):
    active_polls = Poll.objects.annotate(
       used = Exists(
           Poll.users.through.objects.filter(
               poll_id=OuterRef('id'),
               user_id=request.user.id
           ))
    ).filter(active=True)
    serializer = PollSerial(active_polls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerial(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def log_out(request):
    try:
        logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_poll(request, pk):
    try:
        poll = Poll.objects.get(id=pk)
        poll.delete()
        return Response({"message": "Poll deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Poll.DoesNotExist:
        return Response({"error": "Poll not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerial(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote_option(request, option_id):
    option = get_object_or_404(Option, id=option_id)
    option.vote()
    serializer = OptionSerial(option)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote(request, poll_id, option_id):
    try:
        poll = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        return Response({"error": "Poll not found."}, status=status.HTTP_404_NOT_FOUND)
    try:
        option = Option.objects.get(id=option_id, poll=poll)
    except Option.DoesNotExist:
        return Response({"error": "Option not found for this poll."}, status=status.HTTP_404_NOT_FOUND)
    option.count += 1
    option.save()
    poll.total_count += 1
    poll.save()
    return Response({"message": "Vote counted successfully."}, status=status.HTTP_200_OK)

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
# "password2":"pp123pp."
# }




