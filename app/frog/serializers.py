from core.models import Frog
from rest_framework import serializers


class FrogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frog
        fields = ['id', 'created_at', 'updated_at']
