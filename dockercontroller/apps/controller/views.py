"""Controller views"""

from rest_framework import response, views, viewsets

from .models import Service
from .serializers import ServiceSerializer


class ServicesViewset(viewsets.ReadOnlyModelViewSet):
    """Retrieve services for a given device"""

    serializer_class = ServiceSerializer

    def get_queryset(self):
        """Filter services"""
        return Service.objects.filter(
            device__name=self.kwargs["device_name"], active=True
        )


class ServiceStatusApiView(views.APIView):
    """Update container status"""

    def get_service(self, id):
        """Get service"""
        return Service.objects.get(pk=id)

    def post(self, request):
        """Update container status"""
        remote_containers = self.request.data
        for container in remote_containers:
            service = self.get_service(container["id"])
            if service:
                service.status = container["status"]
                service._meta.not_update_version = True
                service.save()
        return response.Response({"message": "containers updated"})
