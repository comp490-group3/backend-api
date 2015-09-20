from django.contrib.auth.models import User
from .models import Business, Offer, OfferInstance, Punch
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'qrcode')


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        depth = 1


class OfferInstanceSerializer(serializers.HyperlinkedModelSerializer):
    offer = OfferSerializer()

    # user = UserSerializer()
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='pk',
        read_only=True
    )

    class Meta:
        model = OfferInstance
        depth = 2
        fields = ('offer', 'user', 'punch_total', 'claimed', 'claimed_on', 'updated_on', 'created_on')