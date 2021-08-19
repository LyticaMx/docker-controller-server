"""dockercontroller URL Configuration"""
from django.contrib import admin
from django.urls import include, path

from dockercontroller.apps.controller import urls as controller_urls

urlpatterns = [path("", include(controller_urls)), path("admin/", admin.site.urls)]
