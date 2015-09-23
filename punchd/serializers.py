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
        fields = ('url', 'name', 'address', 'location', 'link', 'qrcode')


# class OfferSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Offer
#         depth = 1


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='offerinstance-detail')
    # offer = serializers.HyperlinkedIdentityField(view_name='offer-detail')
    business = serializers.HyperlinkedIdentityField(view_name='business-detail')
    name = serializers.CharField(max_length=255, source='offer.name')
    punch_total_required = serializers.IntegerField(source='offer.punch_total_required', read_only=True)
    business = BusinessSerializer(source='offer.business', read_only=True)
    can_redeem = serializers.ReadOnlyField()
    redeemed = serializers.BooleanField(required=False, read_only=True)
    redeemed_on = serializers.DateTimeField(allow_null=True, required=False, read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)
    created_on = serializers.DateTimeField(read_only=True)

    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='pk',
        read_only=True
    )

    class Meta:
        model = OfferInstance
        depth = 2
        # fields = ('url', 'name', 'offer', 'business', 'user', 'punch_total', 'punch_total_required',
        fields = ('url', 'name', 'business', 'user', 'punch_total', 'punch_total_required',
                  'can_redeem', 'redeemed', 'redeemed_on', 'updated_on', 'created_on')