from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    asd = Group.objects.all()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'group': list(asd.values_list('id', flat=True))
        }
    print(list(asd.values_list('id', flat=True)))
    return render(request, 'account/profile.html', context)
