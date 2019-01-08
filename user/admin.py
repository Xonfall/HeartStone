from django.contrib import admin

from user.models import User


# Define the admin class
class UserAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(User, UserAdmin)
