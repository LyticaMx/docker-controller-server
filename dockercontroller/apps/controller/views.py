"""Controller views"""

from rest_framework import viewsets

from .models import Service
from .serializers import ServiceSerializer


class ServicesViewset(viewsets.ReadOnlyModelViewSet):
    """Retrieve services for a given device"""

    serializer_class = ServiceSerializer

    def get_queryset(self):
        """Filter services"""
        return Service.objects.filter(device__name=self.kwargs["device_name"])
