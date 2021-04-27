from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import People
from .serializers import PeopleSerializer, UserSerializer

content = {'Authentication Error': 'Please Login!'}


class PeopleList(generics.ListAPIView):
    queryset = People.objects.all().order_by('registration_time')
    serializer_class = PeopleSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        _id = get_object_or_404(Token, key=token)
        queryset = People.objects.all().filter(owner=_id.user_id).order_by('registration_time')
        serializer_class = PeopleSerializer(queryset, many=True, context={'request': request})
        return Response(serializer_class.data)


class PeopleDetails(generics.RetrieveUpdateAPIView):
    """
    Shows the details about specific user
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def retrieve(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        _id = get_object_or_404(Token, key=token)
        queryset = People.objects.get(pk=_id.user_id)
        serializer_class = PeopleSerializer(queryset, context={'request': request})
        return Response(serializer_class.data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
