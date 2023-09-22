from django.shortcuts import render, redirect

from catstagram.cats.forms import CatAddForm, CatEditForm, CatDeleteForm
from catstagram.cats.utils import get_cat_by_name_and_username
from catstagram.core.decorator import is_owner
from catstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo



# class UserDetailsView(views.generic.DetailView):
#     template_name = 'accounts/profile-details-page.html'
#     model = CatstagramUserModel
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['is_owner'] = self.request.user == self.object
#         context['cats_count'] = self.object.cat_set.count()
#
#         photos = self.object.photo_set.prefetch_related('photolike_set')
#
#         context['photos_count'] = photos.count()
#         context['likes_count'] = sum(x.photolike_set.count() for x in photos)
#
#         return context


def details_cat(request, username, cat_slug):
    cat = get_cat_by_name_and_username(cat_slug, username)
    photos = [apply_likes_count(photo) for photo in cat.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'cat': cat,
        'photos_count': cat.photo_set.count(),
        'cat_photos': photos,
        'is_owner': cat.user == request.user,
    }

    return render(request, 'cats/cat-details-page.html', context)


def add_cat(request):

    if request.method == 'GET':
        form = CatAddForm()

    else:
        form = CatAddForm(request.POST, request.FILES)

        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, 'cats/cat-add-page.html', context)


def edit_cat(request, username, cat_slug):

    cat = get_cat_by_name_and_username(cat_slug, username)

    if not is_owner(request, cat):
        return redirect('details cat', username=username, cat_slug=cat_slug)

    if request.method == "GET":
        form = CatEditForm(instance=cat)

    else:
        form = CatEditForm(request.POST, request.FILES, instance=cat, )

        if form.is_valid():
            form.save()
            return redirect('details cat', username=username, cat_slug=cat_slug)

    context = {
        'form': form,
        'cat_slug': cat_slug,
        'username': username,
    }

    return render(request, 'cats/cat-edit-page.html', context)


def delete_cat(request, username, cat_slug):

    cat = get_cat_by_name_and_username(cat_slug, username)

    if request.method == "GET":
        form = CatDeleteForm(instance=cat)

    else:
        form = CatDeleteForm(request.POST, instance=cat)

        if form.is_valid():
            form.save()
            return redirect('details user',pk=1)

    context = {
        'form': form,
        'cat_slug': cat_slug,
        'username': username,
    }

    return render(request, 'cats/cat-delete-page.html', context)
