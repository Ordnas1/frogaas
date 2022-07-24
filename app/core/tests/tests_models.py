from django.test import TestCase
from core.models import Frog
from utils.testing_utils import mockedUploadedFrogImage


class FrogTestCase(TestCase):
    """Test cases for frog model"""

    def test_create_from(self):
        """Successfully creates frog on database"""
        Frog.objects.create(
            image=mockedUploadedFrogImage
        )

        self.assertEqual(Frog.objects.count(), 1)
