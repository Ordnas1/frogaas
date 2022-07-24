from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Frog
from frog import serializers

from utils.testing_utils import mockedUploadedFrogImage


def create_frog():
    return Frog.objects.create(image=mockedUploadedFrogImage)


FROG_URL = reverse('frog:frog-list')


class FrogTestCase(TestCase):
    """Frog test cases."""

    def setUp(self):
        self.client = APIClient()

    def test_list_frog(self):
        """Successfully returns frogs"""
        create_frog()
        create_frog()

        res = self.client.get(FROG_URL)
        frogs = Frog.objects.all()

        serializer = serializers.FrogSerializer(frogs, many=True)

        print(serializer.data)
        print(res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
