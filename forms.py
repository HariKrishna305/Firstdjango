from django.forms import Models

from .models import UserDetails

class UserForm(ModelsForm):
    class Meta:
        model=UserDetails