from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoomSerializer, UserSerializer
from base.models import Room, User


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/users',
        'GET /api/users/id'
        'POST /api/users/create-user'
        'POST /api/users/update-user'
        'DELETE /api/users/delete-user/id'
        'GET /api/rooms/',
        'GET /api/rooms/id',
        'POST /api/rooms/create-room'
        'DELETE api/rooms/delete-room/id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def createRoom(request):
    serialize = RoomSerializer(data=request.data)

    if serialize.is_valid():
        serialize.save()

    return Response(serialize.data)


@api_view(['DELETE'])
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()

    return HttpResponse(status=204)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return HttpResponse(status=204)
