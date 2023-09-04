from django.urls import path

from catstagram.common.views import index

urlpatterns = (
    path('home/', index, name='index'),
)