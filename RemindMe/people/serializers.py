from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
        owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        user = User.objects.create_user(username=username, email=email,
                                        password=make_password(validated_data['password']),)
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            instance.user.password = make_password(
                validated_data.get('user').get('password', instance.user.password)
            )
            instance.user.save()
