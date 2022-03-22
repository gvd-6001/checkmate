import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models

from setting.models import Branch


class Panel(models.Model):
    manufacturerChoices = (
        ("Texecom", "Texecom"),
        ("Vighanharta", "Vighanharta"),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    selectBranch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    selectManufacturer = models.CharField(
        choices=manufacturerChoices, max_length=100)
    slugName = models.CharField(max_length=30)
    deviceID = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    ipAddress = models.CharField(max_length=30)
    port = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slugName + " " + self.deviceID

    class Meta:
        verbose_name_plural = "Panel"


class PanelInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    panel = models.OneToOneField(Panel, on_delete=models.CASCADE)
    armStatus = models.BooleanField(default=False, null=True, blank=True)
    zoneStatus = ArrayField(ArrayField(models.CharField(
        max_length=200)), size=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NVR(models.Model):
    manufacturerChoices = (
        ("Hikvision", "Hikvision"),
        ("Milesight", "Milesight"),
        ("Dahua", "Dahua"),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    selectBranch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    selectManufacturer = models.CharField(
        choices=manufacturerChoices, max_length=100)
    slugName = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ipAddress = models.CharField(max_length=100)
    port = models.IntegerField()
    playbackUrl = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slugName + " " + self.selectManufacturer

    class Meta:
        verbose_name_plural = "NVR"


class InfoNVR(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    nvr = models.OneToOneField(NVR, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    deviceID = models.CharField(max_length=200, null=True, blank=True)
    macAddress = models.CharField(max_length=200, null=True, blank=True)
    modelNo = models.CharField(max_length=100, null=True, blank=True)
    hddCapacity = models.CharField(max_length=100, null=True, blank=True)
    freeHdd = models.CharField(max_length=100, null=True, blank=True)
    hddType = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nvr.slugName
