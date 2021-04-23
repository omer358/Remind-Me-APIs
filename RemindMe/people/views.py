from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import People
from .serializers import PeopleSerializer, UserSerializer

content = {'Authentication Error': 'Please Login!'}


class PeopleList(generics.ListAPIView):
    queryset = People.objects.all().order_by('registration_time')
    serializer_class = PeopleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = People.objects.all().filter(owner=request.user.id).order_by('registration_time')
        serializer_class = PeopleSerializer(queryset,many=True, context={'request': request})
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)


class PeopleDetails(generics.RetrieveUpdateAPIView):
    """
    Shows the details about specific user
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
