import os

from django import forms

from catstagram.common.models import PhotoLike, PhotoComment
from catstagram.core.form_mixins import DisabledFormMixin
from catstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user',)
        ordering = ('pk',)


class PhotoAddForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo')


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    class Meta:
        model = Photo
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        photo_path = self.instance.photo.path
        if commit:
            self.instance.tagged_cats.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()
            self.instance.delete()
            os.remove(photo_path)
        else:
            pass
        return self.instance
