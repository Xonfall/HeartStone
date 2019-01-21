from django import forms
from . import models

class CreateGuild(forms.ModelForm):
    class Meta:
        model = models.Guild
        fields = ['guild_name','guild_description','guild_limit','guild_logo']