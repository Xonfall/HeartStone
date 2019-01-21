from django.contrib import admin

from forum.models import Forum, Topic, Post


# Register your models here.
# Define the admin class
class ForumAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, ForumAdmin)
admin.site.register(Post, ForumAdmin)
