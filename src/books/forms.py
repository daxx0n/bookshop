from django import forms
from . import models



class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = (
            'book_name',
            'picture',
            'book_price',
            'book_author'
        )