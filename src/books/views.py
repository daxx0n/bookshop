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
    paginate_by = 3

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
    
    def form_valid(self, form):
        if form.has_changed():
            if 'picture' in form.changed_data:
                print (form.changed_data)
        return super().form_valid(form)
    
class BookDeleteView (generic.DeleteView):
    model = models.Books
    template_name = "delete_book.html"
    success_url = "/directories/success/"