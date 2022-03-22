from django.urls import path

from . import views

urlpatterns = [
    path('branchList/', views.branchList, name='branchList'),
    path('branchView/<str:id>/', views.branchInfo, name='branchInfo'),
    path('branchInfo/nvrInfo/hikDetail/<str:id>/',
         views.hikStatus, name='hikStatus'),
    path('branchInfo/panelInfo/vighanhartaDetail/<str:id>',
         views.vighanhartaDetail, name='vighanharta')
]
