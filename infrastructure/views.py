from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect

from setting.models import Branch
from .forms import PanelAddForm, NvrAddForm
from .models import Panel, NVR, InfoNVR, PanelInfo
from .tasks import vighZoneStatus


# Create your views here.

# Map Integration.
@login_required(login_url="homepage")
def deviceLoc(request):
    branch_data = Branch.objects.all()
    singleBranch = Branch.objects.first()
    context = {'branch_data': branch_data,
               'singleBranch': singleBranch}
    return render(request, 'infra/deviceLoc.html', context)


# Panel CRUD
@login_required(login_url="homepage")
def devicePanelInfo(request):
    all_devices = PanelInfo.objects.all()
    context = {'all_devices': all_devices}
    return render(request, 'infra/panel/devicePanelInfo.html', context)


@login_required(login_url="homepage")
@permission_required("infrastructure.add_panel", login_url="notAuthorized")
def devicePanelAdd(request):
    panelAddForm = PanelAddForm()
    if request.method == 'POST':
        form = PanelAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Panel Added Successfully')
            return redirect('devicePanelInfo')
    context = {'panelAddForm': panelAddForm}
    return render(request, 'infra/panel/devicePanelAdd.html', context)


@login_required(login_url="homepage")
@permission_required("infrastructure.update_panel", login_url="notAuthorized")
def devicePanelUpdate(request, pk):
    panel_update = Panel.objects.get(id=pk)
    form = PanelAddForm(instance=panel_update)
    if request.method == 'POST':
        form = PanelAddForm(request.POST, instance=panel_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'Panel Updated Successfully')
            return redirect('devicePanelInfo')
    context = {'updateForm': form, 'panel_Update': panel_update}
    return render(request, 'infra/panel/devicePanelUpdate.html', context)


@login_required(login_url="homepage")
@permission_required("infrastructure.delete_panel", login_url="notAuthorized")
def devicePanelDelete(request, pk):
    panDelete = Panel.objects.get(id=pk)
    panDelete.delete()
    messages.success(request, 'Panel Deleted Successfully')
    return redirect("devicePanelInfo")


# NVR CRUD
@login_required(login_url="homepage")
def deviceNvrInfo(request):
    # hikHddStatus.delay()
    all_devices = InfoNVR.objects.all()
    context = {'all_devices': all_devices}
    return render(request, 'infra/nvr/deviceNvrInfo.html', context)


@login_required(login_url="homepage")
@permission_required("infrastructure.add_nvr", login_url="notAuthorized")
def deviceNvrAdd(request):
    nvrAddform = NvrAddForm()
    if request.method == "POST":
        form = NvrAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "NVR Added Successfully")
            return redirect('deviceNvrInfo')
    context = {'nvrAddform': nvrAddform}
    return render(request, 'infra/nvr/deviceNvrAdd.html', context)


@login_required(login_url="homepage")
@permission_required("infrastructure.update_nvr", login_url="notAuthorized")
def deviceNvrUpdate(request, pk):
    nvr_update = NVR.objects.get(id=pk)
    form = NvrAddForm(instance=nvr_update)
    if request.method == "POST":
        form = NvrAddForm(request.POST, instance=nvr_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'NVR Updated Successfully')
            return redirect('deviceNvrInfo')
    context = {'updateForm': form, 'nvr_Update': nvr_update}
    return render(request, 'infra/nvr/deviceNvrUpdate.html', context)


# @login_required(login_url="homepage")
@permission_required("infrastructure.delete_nvr", login_url="notAuthorized")
def deviceNvrDelete(request, pk):
    nvrDelete = NVR.objects.get(id=pk)
    nvrDelete.delete()
    messages.success(request, 'NVR Deleted Successfully')
    return redirect("deviceNvrInfo")
