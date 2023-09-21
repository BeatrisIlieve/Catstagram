from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

CatstagramUserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CatstagramUserModel
        fields = ('username', 'email')
        field_classes = {
            'username': UsernameField,
        }
