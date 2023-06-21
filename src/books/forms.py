from django import forms
from . import models



class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = (
            'book_name',
            'picture',
            'book_price',
            'book_author',
            'book_serie',
            'book_genre',
            'book_year',
            'book_page',
            'book_cover',
            'book_isbn',
            'book_weight',
            'book_age',
            'book_publisher',
            'book_quantity'
        )