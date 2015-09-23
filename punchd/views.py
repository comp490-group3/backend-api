from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Business, Offer, OfferInstance
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows businesses to be viewed or edited.
    """
    queryset = Business.objects.all().order_by('pk')
    serializer_class = serializers.BusinessSerializer

    @detail_route(methods=['GET'], permission_classes=[IsAuthenticated])
    def punch(self, request, pk=None):
        business = self.get_object()
        offer_instance = business.punch(request.user)
        if offer_instance is False:
            return Response({'status': False})
        else:
            serializer = serializers.OfferSerializer(offer_instance, context={'request': request})
            return Response(serializer.data)


class OfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = OfferInstance.objects.all().order_by('pk')
    serializer_class = serializers.OfferSerializer

    @detail_route(methods=['GET'], permission_classes=[IsAuthenticated])
    def redeem(self, request, pk=None):
        offer = self.get_object()
        return Response({'status': offer.redeem()})


# class OfferViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows offers to be viewed or edited.
#     """
#     queryset = Offer.objects.all().order_by('pk')
#     serializer_class = serializers.OfferSerializer