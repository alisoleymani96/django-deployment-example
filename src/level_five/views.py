from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'level_Five/index.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.the_user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'level_five/registration.html',
                  {'registered': registered,
                   'user_form': user_form,
                   'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        the_user = authenticate(username=username, password=password)

        if the_user:
            if the_user.is_active:
                login(request, the_user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("the user is not active!")

        else:
            print("someone tried to login and Failed")
            print("password: {}, username: {}".format(username, password))
            return HttpResponse("invalid details")

    else:
        return render(request, 'level_five/login.html', {})

