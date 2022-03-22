import requests
from celery import shared_task
from hikvisionapi import Client

from infrastructure.models import InfoNVR, PanelInfo


@shared_task(bind=True)
def hikHddStatus(self):
    hikNvr = InfoNVR.objects.filter(nvr__selectManufacturer="Hikvision")
    for i in hikNvr:
        fetchData = Client('http://' + str(i.nvr.ipAddress) + ":" + str(i.nvr.port), i.nvr.username,
                           i.nvr.password)
        if fetchData:
            deviceResponse = fetchData.System.deviceInfo(method='get')
            hddResponse = fetchData.ContentMgmt.Storage.hdd(method='get')
            InfoNVR.objects.filter(id=i.id).update(status=True)
            InfoNVR.objects.filter(id=i.id).update(
                deviceID=deviceResponse["DeviceInfo"]["deviceID"])
            InfoNVR.objects.filter(id=i.id).update(
                macAddress=deviceResponse["DeviceInfo"]["macAddress"])
            InfoNVR.objects.filter(id=i.id).update(
                modelNo=deviceResponse["DeviceInfo"]["model"])
            InfoNVR.objects.filter(id=i.id).update(
                hddCapacity=hddResponse['hddList']['hdd']['capacity'])
            InfoNVR.objects.filter(id=i.id).update(
                freeHdd=hddResponse['hddList']['hdd']['freeSpace'])
            InfoNVR.objects.filter(id=i.id).update(
                hddType=hddResponse['hddList']['hdd']['hddType'])
    return "Done"


@shared_task(bind=True)
def vighZoneStatus(self):
    vighPanel = PanelInfo.objects.filter(
        panel__selectManufacturer="Vighanharta")
    for i in vighPanel:
        panelZone = requests.get(
            "http://" + i.panel.ipAddress + ":" + str(i.panel.port) + "/api/GetZoneStatus/" + i.panel.deviceID).json()
        if panelZone:
            # Extracting Zone Data from response
            ZoneData = panelZone[0]['data']
            # Converting single string into multiple according to regx
            ZoneSplitting = []
            for l in range(0, len(ZoneData), 5):
                ext = ZoneData[l:l + 4]
                ZoneSplitting.append(ext)
            # According to Documentation applying naming to Zone either Active, Bypass etc...
            ZoneStatus = []
            for j in range(0, len(ZoneSplitting)):
                check = ZoneSplitting[j][-1]
                if check == 'U':
                    ZoneStatus.append("Un-installed")
                elif check == "B":
                    ZoneStatus.append("Zone Bypassed")
                elif check == "R":
                    ZoneStatus.append("Zone Restore")
                else:
                    ZoneStatus.append("Zone Active")
            PanelInfo.objects.filter(id=i.id).update(zoneStatus=ZoneStatus)
    return "Done"
