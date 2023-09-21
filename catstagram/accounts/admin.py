from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from catstagram.accounts.forms import UserEditForm, UserCreateForm

CatstagramUserModel = get_user_model()


@admin.register(CatstagramUserModel)
class CatstagramUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {
             'fields': (
                 'first_name',
                 'last_name',
                 'email',
                 'gender',
             )}),
        ('Permissions',
         {
             'fields': (
                 'is_active',
                 'is_staff',
                 'is_superuser',
                 'groups',
                 'user_permissions',
             ),
         },
         ),
        ('Important dates',
         {
             'fields': (
                 'last_login',
                 'date_joined',
             )}),
    )
