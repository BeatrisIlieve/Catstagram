from django.contrib.auth import get_user_model, login
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from catstagram.accounts.forms import UserCreateForm
from catstagram.accounts.models import Profile

CatstagramUserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index', )

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('login user', )


class UserDetailsView(DetailView):
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


class UserEditView(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = Profile
    fields = ('first_name', 'last_name',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = CatstagramUserModel
    success_url = reverse_lazy('index')
