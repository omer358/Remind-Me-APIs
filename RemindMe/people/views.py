from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import People
from .serializers import PeopleSerializer, UserSerializer


class PeopleList(generics.ListCreateAPIView):
    queryset = People.objects.all().order_by('registration_time')
    serializer_class = PeopleSerializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            queryset = People.objects.all().order_by('registration_time')
            serializer_class = PeopleSerializer(queryset, many=True, context={'request': request})
            print(request.build_absolute_uri())
            return Response(serializer_class.data)
        else:
            content = {'Authentication Error': 'Please Login!'}
            return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)


class PeopleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            queryset = User.objects.all().order_by('id')
            serializer_class = UserSerializer(queryset, many=True)
            return Response(serializer_class.data)
        else:
            content = {'Authentication Error': 'Please Login!'}
            return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)
