from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('carRegister.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('authController.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
