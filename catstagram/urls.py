from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catstagram.common.urls')),
    path('accounts/', include('catstagram.accounts.urls')),
    path('cats/', include('catstagram.cats.urls')),
    path('photos/', include('catstagram.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
