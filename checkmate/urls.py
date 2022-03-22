from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('staff/', include('staff.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('infra/', include('infrastructure.urls')),
    path('setup/', include('setting.urls')),
    path('geo/', include('geography.urls')),
    path('surv/', include('surveillance.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
