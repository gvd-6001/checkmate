from django.urls import path

from . import views

urlpatterns = [
    path('nvr/hikNvrAlerts/', views.hikNvrAlerts, name='hikNvrAlerts'),
]
