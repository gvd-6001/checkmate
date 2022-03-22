from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from infrastructure.models import Panel, InfoNVR, PanelInfo
from setting.models import Branch


# Create your views here.
@login_required(login_url="homepage")
def branchList(request):
    branch_detail = Branch.objects.all()
    context = {'branch_detail': branch_detail}
    return render(request, 'geography/branchList.html', context)


@login_required(login_url="homepage")
def branchInfo(request, id):
    branch_all_info = Branch.objects.get(id=id)  # Branch Info
    panel_all_info = Panel.objects.filter(selectBranch=id)  # Branch Panel Info
    nvr_all_info = InfoNVR.objects.filter(
        nvr__selectBranch=id)  # Branch NVR Info
    context = {'branch_all_info': branch_all_info,
               'panelInfo': panel_all_info,
               'nvrInfo': nvr_all_info}
    return render(request, 'geography/branch-info.html', context)


@login_required(login_url="homepage")
def hikStatus(request, id):
    branch_all_info = Branch.objects.get(id=id)  # Branch Info
    hik_nvr = InfoNVR.objects.filter(nvr__selectBranch=id).filter(
        nvr__selectManufacturer="Hikvision")  # Branch NVR Info
    context = {'branch_all_info': branch_all_info,
               'hikNvrInfo': hik_nvr}
    return render(request, 'geography/infraDetails/hikDetail.html', context)


@login_required(login_url="homepage")
def vighanhartaDetail(request, id):
    branch_all_info = Branch.objects.get(id=id)
    panel_all_info = PanelInfo.objects.filter(panel__selectBranch=id).filter(
        panel__selectManufacturer="Vighanharta")  # Branch Panel Info
    # if request.GET.get('ArmPanel') == "ArmPanel":
    #     armPanel = PanelInfo.objects.filter(
    #         id=request.GET.get('PanelID')).update(armStatus=True)
    #     print("armPanel:", armPanel)
    #     # armStatus = requests.get()

    # if request.GET.get('DisArmPanel') == "DisArmPanel":
    #     disarmPanel = PanelInfo.objects.filter(
    #         id=request.GET.get('PanelID')).update(armStatus=False)
    #     print("disarmPanel:", disarmPanel)

    context = {'branch_all_info': branch_all_info,
               'panelInfo': panel_all_info}
    return render(request, 'geography/infraDetails/vighanhartaDetail.html', context)
