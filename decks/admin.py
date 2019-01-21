from django.contrib import admin

from decks.models import Deck


# Register your models here.
# Define the admin class
class DecksAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Deck, DecksAdmin)
