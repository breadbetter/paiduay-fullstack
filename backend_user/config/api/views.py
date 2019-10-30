from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
# from rest_framework import filters
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
class UserFirstname(viewsets.ModelViewSet):
    lookup_field = 'first_name'
    # search_fields = ['first_name']
    # filter_backends = (filters.SearchFilter)
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserLastname(viewsets.ModelViewSet):
    lookup_field = 'last_name'
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
class UserEmail(viewsets.ModelViewSet):
    lookup_field = 'email'
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
class UserGender(viewsets.ModelViewSet):
    lookup_field = 'gender'
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
class UserAge(viewsets.ModelViewSet):
    lookup_field = 'age'
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class PurchaseList(generics.ListAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         first_name = self.kwargs['first_name']
#         return User.objects.filter(purchaser__first_name=first_name)