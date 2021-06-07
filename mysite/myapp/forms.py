from django import forms
from django.core.validators import validate_slug

from . import models

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
        validators=[
            validate_slug, 
            must_be_bob, 
            must_be_caps,
            must_be_clean
            ]
    )

    def save(self):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion_field"]
        suggestion_instance.save()
        return suggestion_instance