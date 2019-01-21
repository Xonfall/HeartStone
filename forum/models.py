from django.db import models
from user.models import User
from django.conf import settings


# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    lock = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def getTopics(self):
        topics = Topic.objects.filter(category=self, status='S')
        return topics

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(default='S', max_length=1)
    category = models.ForeignKey(Forum, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default='0')

    def getComments(self):
        comments = Post.objects.filter(topic=self, parent=None)
        return comments

    def getTopicsUser(self):
        users = User.objects.filter(id=self.created_by.id)
        return users

    def getAllComments(self):
        comments = Post.objects.filter(topic=self)
        return comments

    def getLastComments(self):
        comments = Post.objects.filter(topic=self).order_by('-created_on').first()
        return comments

    def getForum(self):
        forum = Forum.objects.filter(id=self.category_id)
        return forum

    def __str__(self):
        return self.title


class Post(models.Model):
    comment = models.TextField(null=True, blank=True)
    commented_by = models.ForeignKey(User, related_name="post_by", on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name="topic_comments", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
