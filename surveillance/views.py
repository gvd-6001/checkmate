from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import HikNvrAlert
from .tasks import fetch_post_data

# Create your views here.


@login_required(login_url="homepage")
def hikNvrAlerts(request):
    alerts = HikNvrAlert.objects.all()
    context = {"alerts": alerts}
    return render(request, 'surveillance/nvr/hikNvrAlerts.html', context)
