from django.urls import path

from . import views

urlpatterns = [
    path('deviceLoc/', views.deviceLoc, name='deviceLoc'),
    path('devicePanelInfo/', views.devicePanelInfo, name='devicePanelInfo'),
    path('devicePanelInfo/devicePanelAdd/',
         views.devicePanelAdd, name='devicePanelAdd'),
    path('devicePanelInfo-update/<str:pk>/',
         views.devicePanelUpdate, name='devicePanelUpdate'),
    path('devicePanelInfo-delete/<str:pk>/',
         views.devicePanelDelete, name='devicePanelDelete'),
    path('deviceNvrInfo/', views.deviceNvrInfo, name='deviceNvrInfo'),
    path('deviceNvrInfo/deviceNvrAdd/', views.deviceNvrAdd, name='deviceNvrAdd'),
    path('deviceNvrInfo-update/<str:pk>/',
         views.deviceNvrUpdate, name='deviceNvrUpdate'),
    path('deviceNvrInfo-delete/<str:pk>/',
         views.deviceNvrDelete, name='deviceNvrDelete'),
]
