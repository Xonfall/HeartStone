from django.contrib import admin
from cards.models import Cards


# Register your models here.
# Define the admin class
class CardsAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Cards, CardsAdmin)
