# -*- coding: utf-8 -*-
#from django.contrib.auth.models import User
from .models import CustomUser 
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ( 'first_name', 'last_name', 'gender','age')

class UpdateUserSerializer(UserSerializer):
    def __init__(self, user, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        super(UpdateUserSerializer, self).__init__(*args, **kwargs)
        self.user = user

    def validate_age(self, attrs, source):
        value = attrs[source]
        if not int(value):
            raise serializers.ValidationError("Wrong  age")
        return attrs
