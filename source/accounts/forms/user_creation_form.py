from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import ModelForm

from accounts.models import Profile

User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="email")

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise forms.ValidationError(f"Пожалуйста, заполните хотя бы одно из полей, First name или Last name ")
        return cleaned_data


class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}



class ProfileChangeForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'avatar']