from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

from . import models

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Exists")
    return value

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all uppper case")
    # Always return cleaned data
    return value


def must_be_bob(value):
    if not value.endswith("BOB"):
        raise forms.ValidationError("Must end with BOB")
    return value


def must_be_clean(value):
    if "bad" in value:
        raise forms.ValidationError("Must be clean")
    return value


class SuggestionForm(forms.Form):
    suggestion_field = forms.CharField(
        label="Suggestion",
        required=True,
        max_length=240,
        # validators=[
        #     validate_slug,
        #     must_be_bob,
        #     must_be_caps,
        #     must_be_clean
        #     ]
    )

    def save(self, request):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion_field"]
        suggestion_instance.author = request.user
        suggestion_instance.save()
        return suggestion_instance


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
