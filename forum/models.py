from django.db import models
from user.models import User
from django.conf import settings

STATUS = (
    ('Draft', 'Draft'),
    ('Writed', 'Writed'),
    ('Disabled', 'Disabled'),
)


# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    lock = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True)

    def get_topics(self):
        topics = Topic.objects.filter(category=self, status='Writed')
        return topics

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()
    created_by = models.ForeignKey(User)
    status = models.CharField(choices=STATUS, max_length=10)
    category = models.ForeignKey(Forum)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    no_of_views = models.IntegerField(default='0')

    def get_comments(self):
        post = Post.objects.filter(topic=self, parent=None)
        return post

    def get_all_comments(self):
        post = Post.objects.filter(topic=self)
        return post

    def get_last_comment(self):
        post = Post.objects.filter(topic=self).order_by('-updated_on').first()
        return post

    def get_topic_users(self):
        post_user_ids = Post.objects.filter(topic=self).values_list('post_by', flat=True)
        return post_user_ids

    def __str__(self):
        return self.title


class Post(models.Model):
    comment = models.TextField(null=True, blank=True)
    commented_by = models.ForeignKey(User, related_name="post_by")
    topic = models.ForeignKey(Topic, related_name="topic_comments")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="comment_parent")

    def get_comments(self):
        post = self.post_parent.all()
        return post
