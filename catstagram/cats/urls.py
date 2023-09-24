from django.urls import path, include

from catstagram.cats.views import CatAddView, delete_cat, details_cat, edit_cat

urlpatterns = (
    path('add/', CatAddView.as_view(), name='add cat'),
    path('<str:username>/cat/<slug:cat_slug>/', include([
        path('', details_cat, name='details cat'),
        path('delete/', delete_cat, name='delete cat'),
        path('edit/', edit_cat, name='edit cat'),
    ]))
)