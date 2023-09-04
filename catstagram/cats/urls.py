from django.urls import path, include

from catstagram.cats.views import add_cat, delete_cat, details_cat, edit_cat

urlpatterns = (
    path('add/', add_cat, name='add cat'),
    path('<str:username>/cat/<cat_name>/', include([
        path('', details_cat, name='details cat'),
        path('delete/', delete_cat, name='delete cat'),
        path('edit/', edit_cat, name='edit cat'),
    ]))
)