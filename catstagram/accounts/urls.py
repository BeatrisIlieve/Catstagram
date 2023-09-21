from django.urls import path, include

from catstagram.accounts.views import delete_user, details_user, edit_user, SignInView, SignUpView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        path('delete/', delete_user, name='delete user'),
        path('edit/', edit_user, name='edit user'),
    ])),
)
