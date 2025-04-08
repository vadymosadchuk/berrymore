from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django import forms

from app.models import User
from app.common import selectable_user_permissions


class UserCreateForm(forms.ModelForm):
    user_permissions = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Permission.objects.filter(content_type__app_label='app', codename__in=selectable_user_permissions)
    )
    email = forms.EmailField()
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password_confirmation = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput,
    )

    def clean(self):
        data = super().clean()
        if data['password'] != data['password_confirmation']:
            raise ValidationError('Confirmation password does not match')
        return data

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirmation', 'email', 'first_name', 'last_name', 'user_permissions']
