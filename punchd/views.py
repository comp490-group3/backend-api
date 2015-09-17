from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Business
from .serializers import UserSerializer, BusinessSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows businesses to be viewed or edited.
    """
    queryset = Business.objects.all().order_by('pk')
    serializer_class = BusinessSerializer

