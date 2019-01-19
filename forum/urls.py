from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forum_index, name="forum_index"),
    path('views/<int:id>', views.forum_topics, name="forum_topics"),
    path('topic/<int:id>', views.forum_topic, name="forum_topic"),
    path('newtopic/<int:id>', views.forum_newTopic, name="forum_newTopic"),
    path('comtopic/<int:id>', views.forum_comTopic, name="forum_comTopic"),
    path('blockforum/<int:id>', views.forum_block, name="forum_block"),
    path('unblockforum/<int:id>', views.forum_unblock, name="forum_unblock"),
    path('deltopic/<int:id>', views.forum_deltopic, name="forum_deltopic"),
]