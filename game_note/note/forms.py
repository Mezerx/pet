from django import forms
from .models import User

class AddUsers(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'