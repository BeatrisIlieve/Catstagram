from django.urls import path

from catstagram.cats.views import add_cat, delete_cat, details_cat, edit_cat

urlpatterns = (
    path('add/', add_cat, name='add cat'),
    path('delete/', delete_cat, name='delete cat'),
    path('details/', details_cat, name='details cat'),
    path('edit/', edit_cat, name='edit cat'),
)