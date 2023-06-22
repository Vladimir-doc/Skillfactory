from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from .forms import SignUpForm, UserForm, ProfileForm


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')


@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'user': request.user})
