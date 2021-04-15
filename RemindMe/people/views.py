from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import People
from .serializers import PeopleSerializer, UserSerializer


class PeopleList(generics.ListCreateAPIView):
    queryset = People.objects.all().order_by('registration_time')
    serializer_class = PeopleSerializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            queryset = People.objects.all().order_by('registration_time')
            serializer_class = PeopleSerializer(queryset, many=True)
            return Response(serializer_class.data)
        else:
            queryset = People.objects.all().order_by('registration_time')
            serializer_class = PeopleSerializer(queryset, many=True)
            return Response(serializer_class.data, status.HTTP_405_METHOD_NOT_ALLOWED)



class PersonDetails(generics.GenericAPIView):
    pass


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
