from django.contrib import admin

from catstagram.cats.models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass
