from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import TopicForm, PostForm

# Create your views here.
from forum.models import Forum, Topic, Post
from user.models import User


def forum_index(request):
    categories_list = Forum.objects.all()

    return render(request, 'forum_index.html', {'queryset': categories_list})


def forum_topics(request, id):
    forum = Forum.objects.filter(id=id)
    topic_list = Topic.objects.filter(category_id=id)

    return render(request, 'forum_topics.html', {'forum_set': forum, 'queryset': topic_list, 'id': id})


def forum_topic(request, id):
    topic_list = Topic.objects.filter(id=id)

    for pet in topic_list:
        forum = Forum.objects.filter(id=pet.category_id)

    return render(request, 'forum_topic.html', {'forum_set': forum, 'topic_list': topic_list, 'id': id})


@login_required
def forum_comTopic(request, id):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            tamere = form.save(commit=False)
            tamere.commented_by_id = request.user.id
            tamere.topic_id = id
            tamere.save()

            return redirect('forum_index')
    else:
        form = PostForm()
        topic_list = Topic.objects.filter(id=id)
        for pet in topic_list:
            forum = Forum.objects.filter(id=pet.category_id)

    return render(request, 'forum_comtopic.html', {'forum_set': forum, 'form': form})


@login_required
def forum_newTopic(request, id):
    forum = Forum.objects.filter(id=id)
    if request.POST:
        form = TopicForm(request.POST)
        if form.is_valid():
            tamere = form.save(commit=False)
            tamere.created_by_id = request.user.id
            tamere.category_id = id
            tamere.save()

            return redirect('forum_index')
    else:
        form = TopicForm()

    return render(request, 'forum_newtopic.html', {'forum_set': forum, 'form': form})

def forum_block(request, id):
    if request.user.is_superuser:
        Forum.objects.filter(id=id).update(lock=True)
        return redirect('forum_index')
    else:
        return redirect('forum_index')

def forum_unblock(request, id):

    if request.user.is_superuser:
        Forum.objects.filter(id=id).update(lock=False)
        return redirect('forum_index')
    else:
        return redirect('forum_index')

def forum_deltopic(request, id):
    if request.user.is_superuser:
        topic_list = Topic.objects.filter(id=id)
        for pet in topic_list:
            Post.objects.filter(topic_id=pet.id).delete()
        Topic.objects.filter(id=id).delete()
        return redirect('forum_index')
    else:
        return redirect('forum_index')
