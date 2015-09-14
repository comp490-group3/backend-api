from django.conf import settings
from django.db import models

# class Account(models.Model):
#     user = models.OneToOneField(User)
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#     punches = models.ManyToManyField(Punch, through='OfferInstance')


class Business(models.Model):
    name = models.CharField(max_length=255)
    # - location

    def __unicode__(self):
        return self.name

    @property
    def qrcode(self):
        return 'https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=punchd%%3A%%2F%%2F%s&choe=UTF-8' % self.pk

    class Meta:
        verbose_name_plural = "Businesses"


class Offer(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=255)
    punch_total_required = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # editedon =
    # timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.name


class OfferInstance(models.Model):
    offer = models.ForeignKey(Offer)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    claimed = models.BooleanField(default=False)

    def redeem(self):
        """
        Redeem an offer

        :return: True on success, False on failure
        """
        if self.punch_total == self.offer.punch_total_required:
            self.claimed = True
            return True
        else:
            # raise AttributeError("Insufficient punches")  #TODO change error type
            return False

    # def punch_total(self):
        # return

    # created_on = models.DateTimeField(auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now=True)
    # claimed_on = models.DateTimeField(null=True, blank=True)

    # - count
    # - timestamp


class Punch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    business = models.ForeignKey(Business)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Punches"


