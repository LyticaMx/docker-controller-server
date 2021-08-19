"""Module to register controller models in admin"""
from django.contrib import admin

from .models import Device, Service, ServiceDefinition


class ServiceInline(admin.TabularInline):
    """Stacked form for categories"""

    model = Service


class DeviceAdmin(admin.ModelAdmin):
    """Show device model with services"""

    model = Device
    inlines = [ServiceInline]


admin.site.register(Device, DeviceAdmin)
admin.site.register(ServiceDefinition)
