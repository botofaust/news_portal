from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect

from django.views.generic import UpdateView

from .forms import UserProfileForm


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/user_profile_update.html'
    form_class = UserProfileForm


@login_required
def make_author(request):
    if not request.user.groups.filter(name='authors').exists():
        authors_group = Group.objects.get(name='authors')
        authors_group.user_set.add(request.user)
    return redirect('/')
