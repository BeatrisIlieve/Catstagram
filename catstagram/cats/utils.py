from catstagram.cats.models import Cat


def get_cat_by_name_and_username(cat_slug, username):
    return Cat.objects.get(slug=cat_slug, user__username=username,)