from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

CatstagramUserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CatstagramUserModel
        fields = ('username', 'email')
        field_classes = {
            'username': UsernameField,
        }


class UserEditForm(UserChangeForm):
    class Meta:
        model = CatstagramUserModel
        fields = '__all__'
        field_classes = {
            'username': UsernameField,
        }
