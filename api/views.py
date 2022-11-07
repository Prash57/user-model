from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from base.models import *
from base.forms import MessageForm
from rest_framework import status


@api_view(['GET', 'POST'])
def getRoutes(request):
    routes = [
        {'GET': '/api/profiles'},
        {'GET': '/api/inbox'},
        {'GET': '/api/verify'},
    ]
    return Response(routes)


@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProfile(request, pk):
    profiles = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profiles, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def editProfile(request, pk):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getInbox(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def viewMessage(request, pk):
    messages = Message.objects.get(id=pk)
    serializer = MessageSerializer(messages, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createMessage(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    message.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def verifyUser(request, pk):
    identification = Identification.objects.get(id=pk)
    serializer = IdentificationSerializer(identification, many=False)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def verifyUsers(request):
    identification = Identification.objects.all()
    serializer = IdentificationSerializer(identification, many=True)
    return Response(serializer.data)
