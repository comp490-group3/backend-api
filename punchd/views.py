from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import Business, Offer, OfferInstance
from .permissions import IsOwner, IsAdminOrOwner
from . import serializers


class BusinessListView(ListView):
    model = Business


class BusinessDetailView(DetailView):
    model = Business


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class BusinessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows businesses to be viewed or edited.
    """
    queryset = Business.objects.all().order_by('pk')
    serializer_class = serializers.BusinessSerializer

    @detail_route(methods=['POST', 'GET'])  # TODO remove GET
    def punch(self, request, pk=None):
        """
        Punch a business' first active offer
        """
        business = self.get_object()
        offer_instance = business.punch(request.user)
        if offer_instance is False:
            return Response({'status': False})
        else:
            serializer = serializers.OfferSerializer(offer_instance, context={'request': request})
            return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class OfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = OfferInstance.objects.all().order_by('-pk')
    serializer_class = serializers.OfferSerializer
    # permission_classes = (permissions.IsAuthenticated, IsAdminOrOwner)  # TODO change to IsOwner

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     if self.request.user.is_staff:
    #         return OfferInstance.objects.all()
    #     else:
    #         return OfferInstance.objects.filter(user=self.request.user)

    @detail_route(methods=['POST', 'GET'])  # TODO remove GET
    def redeem(self, request, pk=None):
        """
        Redeem an offer
        """
        offer = self.get_object()
        return Response({'status': offer.redeem()})

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


# class OfferViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows offers to be viewed or edited.
#     """
#     queryset = Offer.objects.all().order_by('pk')
#     serializer_class = serializers.OfferSerializer