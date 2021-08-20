"""Controller urls"""


from django.urls import path

from .views import ServiceStatusApiView, ServicesViewset

services_list = ServicesViewset.as_view({"get": "list"})
services_update = ServiceStatusApiView.as_view()

urlpatterns = [
    path("services/update-status", services_update),
    path("services/<str:device_name>", services_list),
]
