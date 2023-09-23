from django import views
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from catstagram.accounts.forms import UserCreateForm
from catstagram.photos.models import Photo

CatstagramUserModel = get_user_model()


class SignUpView(views.generic.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index',)


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('index',)


class UserDetailsView(views.generic.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = CatstagramUserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['cats_count'] = self.object.cat_set.count()

        photos = self.object.photo_set.prefetch_related('photolike_set')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        return context


class UserEditView(views.generic.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = CatstagramUserModel
    fields = ('first_name', 'last_name', 'email', 'gender', )

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.generic.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = CatstagramUserModel
    success_url = reverse_lazy('index')
