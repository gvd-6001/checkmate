from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.NVR)
admin.site.register(models.InfoNVR)
admin.site.register(models.Panel)
admin.site.register(models.PanelInfo)