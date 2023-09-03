from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('catstagram.accounts.urls')),
    path('cats/', include('catstagram.cats.urls')),
    path('common/', include('catstagram.common.urls')),
    path('photos/', include('catstagram.photos.urls')),
]
