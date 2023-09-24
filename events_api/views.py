from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import permissions, status, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from events_api.permissions import IsEventCreatorOrReadOnly
from events_api.serializers import CustomUserSerializer, EventSerializer
from events_site.models import Event, CustomUser


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@permission_classes([IsAuthenticated])
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


@permission_classes([IsAuthenticated, IsEventCreatorOrReadOnly])
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def join_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.participants.add(request.user)
    return Response({'status': 'join success'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def disjoin_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.participants.remove(request.user)
    return Response({'status': 'disjoin success'}, status=status.HTTP_200_OK)