from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from catstagram.accounts.forms import UserCreateForm, UserEditForm
from catstagram.accounts.models import Profile

CatstagramUserModel = get_user_model()


@admin.register(CatstagramUserModel)
class CatstagramUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'last_login', ]
    list_filter = ()
    add_form = UserCreateForm

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (

                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(Profile)
class EditCatstagramUserAdmin(admin.ModelAdmin):
    ordering = ('first_name',)
    list_display = ['first_name', 'last_name']
    list_filter = ()
    form = UserEditForm
    add_fieldsets = (
        None,
        {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name',),
        },
    ),

# @admin.register(CatstagramUserModel)
# class CatstagramUserAdmin(UserAdmin):
#     form = UserEditForm
#     add_form = UserCreateForm

# fieldsets = (
#     (None, {'fields': ('username', 'password')}),
#     ('Personal info',
#      {
#          'fields': (
#              'first_name',
#              'last_name',
#              'email',
#              'gender',
#          )}),
#     ('Permissions',
#      {
#          'fields': (
#              'is_active',
#              'is_staff',
#              'is_superuser',
#              'groups',
#              'user_permissions',
#          ),
#      },
#      ),
#     ('Important dates',
#      {
#          'fields': (
#              'last_login',
#              'date_joined',
#          )}),
# )
