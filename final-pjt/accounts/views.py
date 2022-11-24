from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm, ProfileUpdateForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from movies.models import Movie, Genre
from .models import User

import operator

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('accounts:login')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:select')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            p_form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'form': form,
        'p_form': p_form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    pickedmovies = person.like_movies.all()

    users = User.objects.all()
    me = request.user
    matchings = []

    if person.favorite:
        genre = Genre.objects.get(pk=person.favorite)
    else:
        genre = 0

    for user in users:
        if me.favorite == user.favorite:
            matchings.append(user)

    context = {
        'person': person,
        'pickedmovies': pickedmovies,
        'matchings': matchings,
        'genre': genre,
    }

    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        person = User.objects.get(pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')


@require_POST
def modeselect(request, user_pk):
    if request.user.is_authenticated:
        user = User.objects.get(pk=user_pk)
        modeselect = user.modeselect
        if modeselect == False:
            modeselect = True
            user.save()
        else:
            modeselect = False
            user.save()
        context = {
            'modeselect': modeselect,
        }
        return JsonResponse(context)
    return redirect('accounts:login')


@require_POST
def love(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.lovers.filter(pk=me.pk).exists():
                you.lovers.remove(me)
                is_loved = False
            else:
                you.lovers.add(me)
                is_loved = True
            context = {
                'is_loved': is_loved,
            }
            return JsonResponse(context)
        return redirect('accounts:profile', me.username)
    return redirect('accounts:login')


@require_POST
def refuse(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if you != me:
            if me.lovers.filter(pk=you.pk).exists():
                me.lovers.remove(you)
                is_loved = False
            else:
                me.lovers.add(you)
                is_loved = True
            context = {
                'is_loved': is_loved,
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')