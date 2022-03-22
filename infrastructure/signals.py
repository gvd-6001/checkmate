from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import InfoNVR, NVR, Panel, PanelInfo


@receiver(post_save, sender=NVR)
def createNvrProfile(sender, instance, created, **kwargs):
    if created:
        nvr = instance
        InfoNVR.objects.create(
            nvr=nvr
        )
    print("NVR Info created")


@receiver(post_save, sender=Panel)
def createPanelInfo(sender, instance, created, **kwargs):
    if created:
        panel = instance
        PanelInfo.objects.create(
            panel=panel
        )
    print("Panel Data Done")
