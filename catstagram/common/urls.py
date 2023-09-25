from django.urls import path

from catstagram.common.views import index, like_photo, comment_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo'),
)