from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/movies/', include('movie.urls')),
    path('api/customer-service/', include('customer_service.urls')),
    path('api/votes/', include('votes.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
