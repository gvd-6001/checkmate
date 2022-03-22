from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from infrastructure.models import InfoNVR, PanelInfo
from setting.models import Branch
from staff.models import Profile


# Create your views here.
@login_required(login_url="homepage")
def dashboard(request):
    nvrCount = InfoNVR.objects.all().count()
    panelCount = PanelInfo.objects.all().count()
    branchCount = Branch.objects.all().count()
    userCount = Profile.objects.all().count()
    userProfile = Profile.objects.all()
    context = {
        'nvrCount': nvrCount,
        'panelCount': panelCount,
        'branchCount': branchCount,
        'userCount': userCount,
        'userProfile': userProfile
    }
    return render(request, 'dashboard/main.html', context)
