from django.urls import path, include

from catstagram.photos.views import add_photo, PhotoDetailsView, edit_photo, delete_photo

urlpatterns = (
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('', PhotoDetailsView.as_view(), name='details photo'),
        path('edit/', edit_photo, name='edit photo'),
        path('delete/', delete_photo, name='delete photo'),
    ]))
)
