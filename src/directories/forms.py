from django import forms
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
    def save (self):
        models.Author.objects.create()
        