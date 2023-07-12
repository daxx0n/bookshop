from django import forms
from . import models
from django.db.migrations.state import get_related_models_tuples
from .models import Comments
from django.utils.translation import gettext_lazy as _

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
            'book_quantity',
            'is_active',
            'book_rating',
                   
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']