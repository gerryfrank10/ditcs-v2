from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Light

class CreatePersonForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class LightsForm(ModelForm):
    class Meta:
        model = Light
        fields = ['state',]