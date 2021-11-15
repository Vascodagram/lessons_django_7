from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

my_default_errors = {
    'invalid': 'Номер телефона только формата +111111111111'
}


class UserCreateForm(UserCreationForm, forms.ModelForm):
    email = forms.EmailField(required=True)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,12}$', error_messages=my_default_errors)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
