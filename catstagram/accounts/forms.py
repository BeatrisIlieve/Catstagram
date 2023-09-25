from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

from catstagram.accounts.models import Profile

CatstagramUserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CatstagramUserModel
        fields = (CatstagramUserModel.USERNAME_FIELD,)
        field_classes = {
            'username': UsernameField,
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )
        if commit:
            profile.save()

        return user


class UserEditForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',)
        field_classes = {
            'username': UsernameField,
        }

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user
