from django.contrib import admin

from catstagram.common.models import PhotoComment


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass
