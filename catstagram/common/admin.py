from django.contrib import admin

from catstagram.common.models import PhotoComment, PhotoLike


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoLike)
class LikeAdmin(admin.ModelAdmin):
    pass
