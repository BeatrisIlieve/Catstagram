from django.shortcuts import render


def add_cat(request):
    return render(request, 'cats/cat-add-page.html')


def delete_cat(request, username, cat_name):
    return render(request, 'cats/cat-delete-page.html')


def details_cat(request, username, cat_name):
    return render(request, 'cats/cat-details-page.html')


def edit_cat(request, username, cat_name):
    return render(request, 'cats/cat-edit-page.html')
