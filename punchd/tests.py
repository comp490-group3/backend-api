from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from .models import Business, Offer, OfferInstance, Punch


class PunchdTestCase(TestCase):
    def setUp(self):
        self.business = Business.objects.create(name="Freudian Sip")

    def test_create_offer(self):
        """Tests a businesses offers"""

        self.assertEqual(self.business.offer_set.all().count(), 0)
        self.business.offer_set.create(
            name="Free coffee",
            punch_total_required=5
        )
        self.assertEqual(self.business.offer_set.all().count(), 1)

    def test_claim_offer_instance(self):
        """Tests claiming an OfferInstance"""

        # user = settings.AUTH_USER_MODEL

        user = User.objects.create_user(
            username='user', email='user@example.com', password='top_secret'
        )

        offer = self.business.offer_set.create(
            name="Free coffee",
            punch_total_required=5
        )

        offer_instance = OfferInstance.objects.create(
            user=user,
            offer=offer,
            claimed=False,
        )

        self.assertEqual(offer_instance.can_redeem(), False)
        self.assertEqual(offer_instance.redeem(), False) #TODO should raise error
        self.assertEqual(offer_instance.punch_total, 0)
        self.assertEqual(offer_instance.claimed, False)

        for i in range(0, 5):
            Punch.objects.create(
                user=user,
                business=self.business
            )

        self.assertEqual(offer_instance.punch_total, 5)
        self.assertEqual(offer_instance.can_redeem(), True)
        self.assertEqual(offer_instance.redeem(), True)
        self.assertEqual(offer_instance.claimed, True)

        offer_instance = None
        offer_instance = OfferInstance.objects.get(pk=1)
        self.assertEqual(offer_instance.claimed, True)


    def test_rest_api(self):
        pass
