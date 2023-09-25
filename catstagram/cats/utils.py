from catstagram.cats.models import Cat


def get_cat_by_name_and_username(cat_slug,pk):
    return Cat.objects\
        .filter(slug=cat_slug, user__id=pk,)\
        .get()
