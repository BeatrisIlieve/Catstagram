from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from catstagram.accounts.models import Profile
from catstagram.photos.forms import PhotoAddForm, PhotoEditForm, PhotoDeleteForm
from catstagram.photos.models import Photo

@login_required
def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    user_liked_photo = Photo.objects.filter(pk=pk, user_id=request.user.pk)

    context = {
        'photo': photo,
        'has_user_liked_photo': user_liked_photo,
        'likes_count': photo.photolike_set.count(),
        'is_owner': request.user == photo.user,
    }

    return render(request, 'photos/photo-details-page.html', context, )


@login_required
def add_photo(request):
    if request.method == "GET":
        form = PhotoAddForm()

    else:
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = PhotoEditForm(instance=photo)

    else:
        form = PhotoEditForm(request.POST, instance=photo)

        if form.is_valid():
            form.save()
            return redirect('details photo', pk=pk)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'photos/photo-edit-page.html', context, )


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = PhotoDeleteForm(instance=photo)

    else:
        form = PhotoDeleteForm(request.POST, request.FILES, instance=photo)

        if form.is_valid():
            form.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'photos/photo-delete-page.html', context, )
