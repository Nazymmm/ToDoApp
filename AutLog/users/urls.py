from django.urls import path, include

from users.views import Register

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),

    path('list/',views.list_user_items),
    path('insert_user/',views.insert_user_item,name='insert_user_item'),
    path('delete_user/<int:user_id>/',views.delete_user_item,name='delete_user_item'),
]
