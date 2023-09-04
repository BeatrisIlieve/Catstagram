from django.contrib import admin

from catstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'publication_date', 'tagged_cat')

    def tagged_cat(self, obj):
        tagged_cats = obj.tagged_cats.all()

        if tagged_cats:
            return ', '.join(c.name for c in tagged_cats)

        return 'No tagged cat'
