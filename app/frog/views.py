from core.models import Frog
from frog.serializers import FrogSerializer

from rest_framework import viewsets, mixins


class FrogViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Frog.objects.all()
    serializer_class = FrogSerializer
