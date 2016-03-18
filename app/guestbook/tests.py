from django.test import TestCase

from guestbook.models import Signature


class GuestbookTestCase(TestCase):
    def test_signature_model(self):
        sig = Signature.objects.create(name="John Doe")
        self.assertEqual(Signature.objects.count(), 1)
        self.assertIsInstance(Signature.objects.get(pk=sig.pk), Signature)
