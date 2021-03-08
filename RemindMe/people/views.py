from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import People
from .serializers import PeopleSerializer


class PeopleList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PersonDetails(generics.GenericAPIView):
    pass