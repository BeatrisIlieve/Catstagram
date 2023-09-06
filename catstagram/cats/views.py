from django.shortcuts import render

from catstagram.cats.utils import get_cat_by_name_and_username
from catstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo


def add_cat(request):
    return render(request, 'cats/cat-add-page.html')


def delete_cat(request, username, cat_slug):
    return render(request, 'cats/cat-delete-page.html')


def details_cat(request, username, cat_slug):
    cat = get_cat_by_name_and_username(cat_slug, username)
    photos = [apply_likes_count(photo) for photo in cat.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'cat': cat,
        'photos_count': cat.photo_set.count(),
        'cat_photos': photos,

    }

    return render(request, 'cats/cat-details-page.html', context)


def edit_cat(request, username, cat_slug):
    return render(request, 'cats/cat-edit-page.html')
