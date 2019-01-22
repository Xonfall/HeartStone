from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.template import RequestContext
from django import forms

from cards.models import Card_user, Card
from .forms import MyCustomUserForm, EditForm
from django.http.response import HttpResponse, JsonResponse
from .models import User, Follow
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect("/")


def register(request):
    if request.method == 'POST':
        form = MyCustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)

            for x in range(1, 60):
                insert_cards = Card_user(card_id=x, user_id=request.user.id)
                insert_cards.save()
            return redirect("/")
    else:
        form = MyCustomUserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@csrf_exempt
@login_required(login_url='/user/login/')
def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            user = User.objects.get(id=request.user.id)
            user.username = username
            user.email = email
            user.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'no'})


@login_required(login_url='/user/login/')
def show_profile(request, username, number_of_posts=2):
    nowUser = User.objects.get(id=request.user.id)
    try:
        user = User.objects.get(username=username)
    except:
        user = None
    if user is not None:
        followers = User.objects.filter(follow=user)

        get_cards = Card.objects.filter(card_user__in=Card_user.objects.filter(user_id=user.id))

        if user.username == nowUser.username:
            return render(request, "user/profile.html",
                          {"user": nowUser, "owner": True, "other": user, "followers": followers,
                           "is_scroll": True})
        else:
            if user in nowUser.follow.all():
                return render(request, "user/profile.html",
                              {"user": nowUser, "owner": False, "follows": True, "other": user
                                  , "followers": followers, "is_scroll": True, 'cards': get_cards})
            else:
                return render(request, "user/profile.html",
                              {"user": nowUser, "owner": False, "follows": False, "other": user
                                  , "followers": followers, "is_scroll": True})
    else:
        return redirect("/")


@csrf_exempt
def follow(request):
    if request.method == 'POST':
        currentUser = User.objects.get(id=request.user.id)
        username = request.POST.get('followed')
        user = User.objects.get(username=username)
        if len(Follow.objects.filter(follower=currentUser, followed=user)) == 0:
            Follow.objects.create(follower=currentUser, followed=user)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'false': 'ok'})


@csrf_exempt
def unfollow(request):
    if request.method == 'POST':
        currentUser = User.objects.get(id=request.user.id)
        username = request.POST.get('followed', '')
        user = User.objects.get(username=username)
        # currentUser.follow.remove(user)
        if len(Follow.objects.filter(follower=currentUser, followed=user)) == 0:
            return
        f = Follow.objects.filter(follower=currentUser, followed=user)
        f.delete()
        return JsonResponse({'status': 'ok'})


@login_required(login_url='/user/login/')
def search_user(request):
    return render(request, 'user/list.html')


def ajax_search(request):
    username = ''

    if request.method == 'GET':
        username = request.GET['username']

    return render_to_response('user/ajax_users.html', {'user_list': find_matching_users(username)},
                              RequestContext(request))


# helper method for AJAX search users, returns a list of the matching users based on search request
def find_matching_users(username=''):
    users = []

    if username:
        users = User.objects.filter(username__contains=username)

    return users
