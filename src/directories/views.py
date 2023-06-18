from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models
from . import forms

#Author

class AuthorListView (generic.ListView):
    template_name = "author_list.html"
    model = models.Author
    paginate_by = 3

class AuthorView (generic.DetailView):
    template_name = "view_authors.html"
    model = models.Author

class AuthorCreateView (generic.CreateView):
    model = models.Author
    form_class = forms.AuthorModelForm
    template_name = "add.html"
    
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()
    
class AuthorUpdateView (generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorModelForm
    template_name = "update.html"
    
    def form_valid(self, form):
        if form.has_changed():
            if 'picture' in form.changed_data:
                print (form.changed_data)
        return super().form_valid(form)
    
class AuthorDeleteView (generic.DeleteView):
    model = models.Author
    template_name = "delete_author.html"
    success_url = "/directories/success/"
    
# Serie

class SerieListView (generic.ListView):
    template_name = "series_list.html"
    model = models.Serie
    paginate_by = 3

class SerieView (generic.DetailView):
    template_name = "view_series.html"
    model = models.Serie

class SerieCreateView (generic.CreateView):
    model = models.Serie
    fields = [
        'serie_name', 'serie_description'
    ]
    template_name = "add.html"
    
class SerieUpdateView (generic.UpdateView):
    model = models.Serie
    fields = [
        'serie_name', 'serie_description'
    ]
    template_name = "update.html"
 
class SerieDeleteView (generic.DeleteView):
    model = models.Serie
    template_name = "delete_series.html"
    success_url = "/directories/success/"
     
# Genres

class GenreListView (generic.ListView):
    template_name = "genres_list.html"
    model = models.Genre
    paginate_by = 2

class GenreView (generic.DetailView):
    template_name = "view_genres.html"
    model = models.Genre

class GenreCreateView (generic.CreateView):
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = "add.html"
    
class GenreUpdateView (generic.UpdateView):
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = "update.html"
  
class GenreDeleteView (generic.DeleteView):
    model = models.Serie
    template_name = "delete_genres.html"  
    success_url = "/directories/success/"
    
#Publishers 

class PublisherListView (generic.ListView):
    template_name = "publishers_list.html"
    model = models.Publisher
    paginate_by = 3

class PublisherView (generic.DetailView):
    template_name = "view_publishers.html"
    model = models.Publisher

class PublisherCreateView (generic.CreateView):
    model = models.Publisher
    fields = [
        'publisher_name', 'publisher_description'
    ]
    template_name = "add.html"
    
class PublisherUpdateView (generic.UpdateView):
    model = models.Publisher
    fields = [
        'publisher_name', 'publisher_description'
    ]
    template_name = "update.html"
 
    
class PublisherDeleteView (generic.DeleteView):
    model = models.Publisher
    template_name = "delete_publishers.html"
    success_url = "/directories/success/"
  
     
# Success page

def success_page(request):
    return render (
        request,
        template_name = "success_page.html",
        context = {"message": "The object was created/updated or deleted succefully!"}
        )

