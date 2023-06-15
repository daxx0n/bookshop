from django import forms
from django.core.exceptions import ValidationError
from . import models


class AddAuthorForm(forms.Form):
    author_firstname = forms.CharField(
        required = True,
        label= "Pls select an author firstname",
        help_text="this is a test helptext"
    )
    author_lastname = forms.CharField( 
        max_length=50, 
        required=True,
        label="pls add an author lastname"
    )
    author_bio = forms.CharField( 
        max_length=50, 
        required=True,
        label="pls add an author biography"
    )
    def save (self):
        models.Author.objects.create()

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'picture',
            'author_firstname', 
            'author_lastname',
            'author_bio'
        )
        