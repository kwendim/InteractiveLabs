from allauth.account.forms import SignupForm
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django import forms
from django.contrib.auth.models import Group


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super(CustomSocialAccountAdapter, self).save_user(request, sociallogin, form)
        group, _ = Group.objects.get_or_create(name='Gamer')
        group.user_set.add(user)
        group.save()
        return user


class RegistrationForm(SignupForm):

    first_name = forms.CharField(max_length=255, required=True,
            label='Name',
            widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))

    field_order = ['email', 'username','first_name', 'last_name', 'password1', 'password2']

    def save(self, request):
        user = super(RegistrationForm, self).save(request)

        return user
