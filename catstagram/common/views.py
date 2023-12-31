from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from catstagram.common.forms import PhotoCommentForm, SearchPhotosForm
from catstagram.common.models import PhotoLike
from catstagram.common.utils import get_photo_url
from catstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from catstagram.photos.models import Photo


def index(request):
    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['cat_name']

    photos = Photo.objects.all()
    if search_pattern:
        photos = photos.filter(tagged_cats__name__icontains=search_pattern)
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


@login_required
def like_photo(request, photo_id):
    user_liked_photo = PhotoLike.objects \
        .filter(photo_id=photo_id, user_id=request.user.pk, )

    if user_liked_photo:
        user_liked_photo.delete()

    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))


@login_required
def comment_photo(request, photo_id, ):
    photo = Photo.objects.filter(pk=photo_id, user_id=request.user.pk,).get()

    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()

    return redirect('details photo', pk=photo_id)
