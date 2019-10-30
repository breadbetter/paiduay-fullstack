from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    search_fields = ['id','first_name','last_name','email','gender','age']
    filter_backends = (filters.SearchFilter,)
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
class UserId(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer   

# class UserFirstname(viewsets.ModelViewSet):
#     lookup_field = 'first_name'
#     # search_fields = ['first_name']
#     # filter_backends = (filters.SearchFilter)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class UserLastname(viewsets.ModelViewSet):
#     lookup_field = 'last_name'
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
# class UserEmail(viewsets.ModelViewSet):
#     lookup_field = 'email'
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
# class UserGender(viewsets.ModelViewSet):
#     lookup_field = 'gender'
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
# class UserAge(viewsets.ModelViewSet):
#     lookup_field = 'age'
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
