from django.conf import settings
from django.db import models
# from django.contrib.gis.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# import datetime

# class Account(models.Model):
#     user = models.OneToOneField(User)
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#     punches = models.ManyToManyField(Punch, through='OfferInstance')


class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location = models.TextField()
    link = models.URLField(verbose_name="URL")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField(auto_now_add=True)

    # objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    @property
    def qrcode(self, height=300, width=300, prefix='punchd%%3A%%2F%%2F'):
        return 'https://chart.googleapis.com/chart?chs=%dx%d&cht=qr&chl=%s%s&choe=UTF-8&chld=H|0' % (height, width, prefix, self.pk)

    def punch(self, user):
        """
        Punch a business' first active offer as a given user
        :param user: User
        :return: OfferInstance on success, False if no active or valid offers
        """
        offer = self.offer_set.filter(active=True).first()

        if not offer:
            return False

        offer_instance, created = OfferInstance.objects.get_or_create(
            user=user,
            offer=offer,
        )

        if offer_instance.redeemed or offer_instance.can_redeem():
            return False

        offer_instance.punches.create(
            user=user,
            business=self
        )
        return offer_instance

    def get_absolute_url(self):
        return reverse('business-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Businesses"


class Offer(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=255)
    punch_total_required = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # editedon =
    # timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('offer-detail', kwargs={'pk': self.pk})

class OfferInstance(models.Model):
    offer = models.ForeignKey(Offer)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    redeemed = models.BooleanField(default=False)
    punches = models.ManyToManyField('Punch') # TODO use architecture with less db overhead
    # timestamp = models.DateTimeField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    redeemed_on = models.DateTimeField(null=True, blank=True)

    def can_redeem(self):
        """
        Can the user redeem an offer?

        :return: True if yes, False if no
        """
        if self.redeemed is False and self.punch_total == self.offer.punch_total_required:
            return True
        else:
            return False

    def redeem(self):
        """
        Redeem an offer

        :return: True on success, False on failure
        """
        if self.can_redeem():
            self.redeemed = True
            self.redeemed_on = timezone.now()
            # self.redeemed_on = datetime.datetime.now()
            self.save()
            return True
        else:
            # raise AttributeError("Insufficient punches")  #TODO change error type
            return False

    @property
    def punch_total(self):
        """
        Total number of times this offer has been punched

        :return: Integer number of times this offer has been punched
        """
        # return Punch.objects.filter(user=self.user, business=self.offer.business).count()
        return self.punches.count()

    @property
    def punch_total_required(self):
        """
        Total number of times this offer needs to be punched to be redeemed

        :return: Integer number of times this offer has to be punched to be redeemed
        """
        return self.offer.punch_total_required

    def __unicode__(self):
        # return u'%s (%d of %d for %s)' % (self.offer.name, self.punch_total, self.offer.punch_total_required, self.user)
        return u'%s (for %s)' % (self.offer.name, self.user)

    class Meta:
        unique_together = ("user", "offer") # Only allow a user to have 1 instance of an offer


class Punch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    business = models.ForeignKey(Business)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s at %s' % (self.user, self.business)

    class Meta:
        verbose_name_plural = "Punches"


