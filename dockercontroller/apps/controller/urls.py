"""Controller urls"""


from django.urls import path

from .views import ServicesViewset

services_list = ServicesViewset.as_view({"get": "list"})

urlpatterns = [
    path("services/<str:device_name>", services_list),
]
