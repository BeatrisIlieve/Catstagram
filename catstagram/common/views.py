from django.shortcuts import render, redirect

from catstagram.common.models import PhotoLike
from catstagram.photos.models import Photo


def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }

    return render(request, 'common/home-page.html', context)


def get_user_liked_photos(photo_id):

    return PhotoLike.objects.filter(photo_id=photo_id)


def like_photo(request, photo_id):

    user_liked_photo = get_user_liked_photos(photo_id)

    if user_liked_photo:
        user_liked_photo.delete()

    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

    redirect_path = redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')
    return redirect_path
