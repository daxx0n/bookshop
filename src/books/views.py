from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views import generic
from django import forms
from . import models
from . import forms



# Create your views here.

class BookListView (generic.ListView):
    template_name = "book_list.html"
    model = models.Books
    paginate_by = 10

class BookView (generic.DetailView):
    template_name = "view_book.html"
    model = models.Books

class BookCreateView (generic.CreateView):
    model = models.Books
    form_class = forms.BookModelForm
    template_name = "add.html"
    
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()
    
class BookUpdateView (generic.UpdateView):
    model = models.Books
    form_class = forms.BookModelForm
    template_name = "update.html"
    
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()
    
class BookDeleteView (generic.DeleteView):
    model = models.Books
    template_name = "delete_book.html"
    success_url = "/directories/success/"