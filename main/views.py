# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import UserSerializer,UpdateUserSerializer
from .models import CustomUser

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
    })

class UserDetail(generics.RetrieveAPIView):
    """
    API endpoint that represents a single user.
    """
    model = CustomUser
    serializer_class = UserSerializer
    lookup_field = 'email'


class GetUser(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = CustomUser
    serializer_class = UserSerializer
    def get_object(self):
        email =  self.request.user
        queryset = None
        if email is not None:
            queryset = CustomUser.objects.get(email=email)
        return queryset

#    @api_view('PATCH'])
#    def edit_time(request):
#        if request.method == 'PATCH':
#    serializer = UpdateUserSerializer(request.user, data=request.DATA, partial=True)
#    if serializer.is_valid():
#        time_entry = serializer.save()
#        return Response(status=status.HTTP_201_CREATED) 
#    return Response(status=status.HTTP_400_BAD_REQUEST) 

class UserList(generics.ListAPIView):
    """
    API endpoint that represents a list of users.
    """
    queryset = CustomUser.objects.all()
    model = CustomUser
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = CustomUser.objects.all()
        age = self.request.QUERY_PARAMS.get('age', None)
        if age is not None:
            queryset = queryset.filter(age=age)

        return queryset

def home(request):
    template = "index.html"
    return render(request, template, locals(), content_type='text/html')

