"""Controller models"""

import time

from django.db import models


def get_unix_timestamp(date):
    """Gets UNIX timestamp"""
    return int(time.mktime(date.timetuple()))


def merge_configs(config_1, config_2):
    """Merge two config dictionaries"""
    # config_1 = dict(config_1)
    for key, value in config_2.items():
        if key in config_1:
            if type(value) is dict:
                merge_configs(config_1[key], value)
            elif type(value) in (int, float, str):
                config_1[key] = config_2[key]
            elif type(value) is list:
                config_1[key].append(config_2[key])
        else:
            config_1[key] = value
    return config_1


class Device(models.Model):
    """A device running a docker host"""

    name = models.CharField(max_length=40, unique=True)

    def __str__(self) -> str:
        """Set device name for admin"""
        return self.name


class ServiceDefinition(models.Model):
    """Docker container definition"""

    name = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    docker_config = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Set service name for admin"""
        return self.name


class CustomDateTimeField(models.DateTimeField):
    """Modified datetime field to control auto_now programatically"""

    def pre_save(self, model_instance, add):
        """pre-save override to be awere of auto now behavour"""
        if getattr(model_instance._meta, "not_update_version", False):
            return models.Field.pre_save(self, model_instance, add)
        return super().pre_save(model_instance, add)


class Service(models.Model):
    """Represents a running container in a device"""

    definition = models.ForeignKey("ServiceDefinition", on_delete=models.CASCADE)
    device = models.ForeignKey("Device", on_delete=models.CASCADE)
    custom_config = models.JSONField(blank=True)
    status = models.CharField(max_length=10, blank=True, editable=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = CustomDateTimeField(auto_now=True)

    @property
    def config(self):
        """Returns docker config for this service"""
        if self.custom_config:
            return merge_configs(self.definition.docker_config, self.custom_config)
        return self.definition.docker_config

    @property
    def version(self):
        """Returns updated at as a UNIX timestamp"""
        definition_version = get_unix_timestamp(self.definition.updated_at)
        service_version = get_unix_timestamp(self.updated_at)
        return f"{definition_version}_{service_version}"

    def __str__(self):
        """Shows id and version in admin"""
        return f"id: {str(self.id)} - version: {str(self.version)}"
