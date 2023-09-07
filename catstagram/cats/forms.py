from django import forms

from catstagram.cats.models import Cat
from catstagram.core.form_mixins import DisabledFormMixin


class CatBaseForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ('name', 'date_of_birth', 'personal_photo')
        labels = {
            'name': 'Cat Name',
            'personal_photo': 'Cat Photo',
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
            # 'personal_photo': forms.ImageField(
            #     attrs={
            #         'placeholder': 'No file chosen',
            #     }
            # ),
        }


class CatAddForm(CatBaseForm):
    pass


class CatEditForm(CatBaseForm):
    pass


class CatDeleteForm(DisabledFormMixin, CatBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
