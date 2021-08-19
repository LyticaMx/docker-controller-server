"""Controller serializers"""
from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    """Returns config to control a given device"""

    class Meta:
        """Fields definition"""

        model = Service
        fields = ["id", "version", "config"]
