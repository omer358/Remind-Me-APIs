from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import People
from .serializers import PeopleSerializer
content = {'Authentication Error': 'Please Login!'}


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all().order_by('registration_time')
    serializer_class = PeopleSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        _id = get_object_or_404(Token, key=token)
        queryset = People.objects.all().filter(owner=_id.user_id).order_by('registration_time')
        serializer_class = PeopleSerializer(queryset, many=True, context={'request': request})
        return Response(serializer_class.data)

    def retrieve(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        _id = get_object_or_404(Token, key=token)
        queryset = People.objects.get(pk=_id.user_id)
        serializer_class = PeopleSerializer(queryset, context={'request': request})
        return Response(serializer_class.data)