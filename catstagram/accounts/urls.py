from django.urls import path, include

from catstagram.accounts.views import delete_user, SignInView, SignUpView, SignOutView, UserDetailsView, EditUserView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', delete_user, name='delete user'),

    ])),
)
