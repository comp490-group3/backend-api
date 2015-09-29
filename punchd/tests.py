from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from .models import Business, Offer, OfferInstance, Punch


class PunchdUserTestCase(TestCase):
    def setUp(self):
        """
        Creates a business and an offer
        """
        self.user = User.objects.create_user(
            username='user', email='user@example.com', password='top_secret'
        )

        self.business = Business.objects.create(name="Freudian Sip", address="12345 Anystreet USA",
                                                location="POINT(-118.5286617 34.2415936)",
                                                link="http://www.csun.edu/", owner=self.user)

        self.offer = self.business.offer_set.create(
            name="Free coffee",
            punch_total_required=5
        )

    def test_new_user(self):
        """
        Verify a new user is created automatically
        """
        pass

    def test_scan_qr_code_without_existing_punches(self):
        # No existing offer instance
        results = OfferInstance.objects.filter(
            user=self.user,
            offer=self.offer,
        ).count()
        self.assertEqual(results, 0)

        offer_instance = self.business.punch(self.user)

        self.assertEqual(offer_instance.can_redeem(), False)
        self.assertEqual(offer_instance.redeem(), False)
        self.assertEqual(offer_instance.punch_total, 1)
        self.assertEqual(offer_instance.redeemed, False)

    def test_scan_qr_code_with_existing_punches(self):
        pass

    def test_scan_invalid_qr_code(self):
        pass

    def test_attempt_redeem_already_redeemed_offer(self):
        """
        Verify an error will occur if the user attempts to punch
        one more time on an offer that has already been redeemed
        """
        for i in range(0, 5):
            offer_instance = self.business.punch(self.user)
        self.assertEqual(offer_instance.redeem(), True)
        self.assertEqual(offer_instance.redeemed, True)

        self.assertEqual(offer_instance.redeem(), False)
        self.assertEqual(offer_instance.redeemed, True)

    def test_attempt_punch_offer_ready_to_redeem(self):
        """
        Verify an error will occur if the user attempts to punch
        one more time on an offer that is ready to be redeemed
        """
        for i in range(0, 5):
            offer_instance = self.business.punch(self.user)

        self.assertEqual(offer_instance.can_redeem(), True)
        self.assertEqual(offer_instance.redeemed, False)
        self.assertEqual(offer_instance.punch_total, 5)

        offer_instance_b = self.business.punch(self.user)
        self.assertEqual(offer_instance_b, False)

        self.assertEqual(offer_instance.can_redeem(), True)
        self.assertEqual(offer_instance.redeem(), True)
        self.assertEqual(offer_instance.punch_total, 5)
        self.assertEqual(offer_instance.redeemed, True)

    def test_attempt_punch_already_redeemed_offer(self):
        """
        Verify an error will occur if the user attempts to punch
        one more time on an offer that has already been redeemed
        """
        for i in range(0, 5):
            offer_instance = self.business.punch(self.user)
        self.assertEqual(offer_instance.redeem(), True)

        offer_instance_b = self.business.punch(self.user)
        self.assertEqual(offer_instance_b, False)

        self.assertEqual(offer_instance.redeem(), False)
        self.assertEqual(offer_instance.punch_total, 5)
        self.assertEqual(offer_instance.redeemed, True)

    def test_redeem_offer(self):
        """Verify a user can redeem an offer"""
        for i in range(0, 4):
            offer_instance = self.business.punch(self.user)
            self.assertEqual(offer_instance.can_redeem(), False)
            self.assertEqual(offer_instance.redeem(), False)
            self.assertEqual(offer_instance.redeemed, False)
            self.assertEqual(offer_instance.punch_total, i+1)

        offer_instance = self.business.punch(self.user)
        self.assertEqual(offer_instance.can_redeem(), True)
        self.assertEqual(offer_instance.punch_total, 5)
        self.assertEqual(offer_instance.redeem(), True)
        self.assertEqual(offer_instance.punch_total, 5)
        self.assertEqual(offer_instance.redeemed, True)


class PunchdSimpleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user2', email='user@example.com', password='top_secret'
        )
        self.business = Business.objects.create(name="Freudian Sip", address="12345 Anystreet USA",
                                                location="POINT(-118.5286617 34.2415936)",
                                                link="http://www.csun.edu/", owner=self.user)

    def test_create_offer(self):
        """Tests a businesses offers"""

        self.assertEqual(self.business.offer_set.all().count(), 0)
        self.business.offer_set.create(
            name="Free coffee",
            punch_total_required=5
        )
        self.assertEqual(self.business.offer_set.all().count(), 1)

    def test_redeeming_offer_instance(self):
        """Tests redeeming an OfferInstance"""

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
            redeemed=False,
        )

        self.assertEqual(offer_instance.can_redeem(), False)
        self.assertEqual(offer_instance.redeem(), False) #TODO should raise error
        self.assertEqual(offer_instance.punch_total, 0)
        self.assertEqual(offer_instance.redeemed, False)

        for i in range(0, 5):
            self.business.punch(user)
            # Punch.objects.create(
            #     user=user,
            #     business=self.business
            # )

        self.assertEqual(offer_instance.punch_total, 5)
        self.assertEqual(offer_instance.can_redeem(), True)
        self.assertEqual(offer_instance.redeem(), True)
        self.assertEqual(offer_instance.redeemed, True)

        offer_instance = None
        offer_instance = OfferInstance.objects.get(pk=1)
        self.assertEqual(offer_instance.redeemed, True)

    def test_rest_api(self):
        pass
