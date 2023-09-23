from django import forms

from catstagram.cats.models import Cat
from catstagram.core.form_mixins import DisabledFormMixin


class CatBaseForm(forms.ModelForm):
    class Meta:
        model = Cat

        fields = ('name', 'date_of_birth', 'personal_photo',)
        labels = {
            'name': 'Cat Name',
            'personal_photo': '',
            'date_of_birth': 'Date of Birth',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Cat Name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
        }

        # help_texts = {
        #     'name': 'Enter your name',
        # }


class CatAddForm(CatBaseForm):
    pass


class CatEditForm(CatBaseForm):
    class Meta:
        model = Cat
        exclude = ('slug', 'user')


class CatDeleteForm(DisabledFormMixin, CatBaseForm):
    class Meta:
        model = Cat

        fields = ('name',)
        labels = {
            'name': 'Cat Name',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Cat Name',
                }
            ),
        }

    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
