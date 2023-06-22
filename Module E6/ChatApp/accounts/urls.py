from django.urls import path

from .views import SignUp, edit_user


urlpatterns = [
    path('profile/', edit_user, name='profile'),
    path('signup/', SignUp.as_view(), name='signup'),
]
