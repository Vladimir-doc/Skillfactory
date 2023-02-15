from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, View
from .forms import SignUpForm
from django.contrib.auth.mixins import PermissionRequiredMixin


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'

    template_name = 'registration/signup.html'


class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')