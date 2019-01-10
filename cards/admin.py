from django.contrib import admin

from cards.models import Card

# Register your models here.
# Define the admin class
class CardsAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Card, CardsAdmin)
