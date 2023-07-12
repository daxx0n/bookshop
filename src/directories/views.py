from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from . import models
from . import forms

#Author

class AuthorListView (generic.ListView):
    template_name = "author_list.html"
    model = models.Author
    paginate_by = 10

class AuthorView (generic.DetailView):
    template_name = "view_authors.html"
    model = models.Author

class AuthorCreateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.CreateView,):
    model = models.Author
    form_class = forms.AuthorModelForm
    template_name = "add.html"
    login_url = reverse_lazy("staff:login")
    context_object_name = 'author_create'
    success_url = reverse_lazy('Home Page')
    success_message = 'Автор был успешно создан!'
    permission_required = "directories.author_create"

    
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()
    
class AuthorUpdateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorModelForm
    template_name = "update.html"
    login_url = reverse_lazy("staff:login")
    success_url = reverse_lazy('Home Page')
    context_object_name = 'author_update'
    success_message = 'Автор был успешно обновлен'
    permission_required = ('directories.change_author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Автор обновлен'
        return context

class AuthorDeleteView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Author
    template_name = "delete_author.html"
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'author_delete'
    success_message = "Автор был успешно удален!"
    permission_required = ('directories.delete_author')
    
# Serie

class SerieListView (generic.ListView):
    template_name = "series_list.html"
    model = models.Serie
    paginate_by = 10

class SerieView (generic.DetailView):
    template_name = "view_series.html"
    model = models.Serie

class SerieCreateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Serie
    fields = [
        'serie_name', 'serie_description'
    ]
    template_name = "add.html"
    success_url = reverse_lazy('directories:series_list')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'serie_create'
    success_message = "Серия успешно создана!"
    permission_required = ('directories.add_serie')
    
class SerieUpdateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Serie
    fields = [
        'serie_name', 'serie_description'
    ]
    template_name = "update.html"
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'serie_update'
    success_message = "Серия была успешно обновлена!"
    permission_required = ('directories.change_serie')
 
class SerieDeleteView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Serie
    template_name = "delete_series.html"
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'serie_delete'
    success_message = "Серия была успешно удалена!"
    permission_required = ('directories.delete_serie')
     
# Genres

class GenreListView (generic.ListView):
    template_name = "genres_list.html"
    model = models.Genre
    paginate_by = 10
    

class GenreView (generic.DetailView):
    template_name = "view_genres.html"
    model = models.Genre

class GenreCreateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = "add.html"
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'genre_create'
    success_message = "Серия была успешно создана!"
    permission_required = ('directories.add_genre')
    
class GenreUpdateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = "update.html"
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'genre_update'
    success_message = "Жанр был успешно обновлен!"
    permission_required = ('directories.change_genre')
  
class GenreDeleteView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Serie
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'genre_delete'
    success_message = "Жанр был успешно удален!"
    permission_required = ('directories.delete_genre')
    
#Publishers 

class PublisherListView (generic.ListView):
    template_name = "publishers_list.html"
    model = models.Publisher
    paginate_by = 10

class PublisherView (generic.DetailView):
    template_name = "view_publishers.html"
    model = models.Publisher

class PublisherCreateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Publisher
    fields = [
        'publisher_name', 'publisher_description'
    ]
    template_name = "add.html"
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'publisher_create'
    success_message = "Издатель был успешно создан!"
    permission_required = ('directories.add_publisher')
    
class PublisherUpdateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Publisher
    fields = [
        'publisher_name', 'publisher_description'
    ]
    template_name = "update.html"
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'publisher_update'
    success_message = "Издатель был успешно обновлен!"
    permission_required = ('directories.change_publisher')
 
    
class PublisherDeleteView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Publisher
    template_name = "delete_publishers.html"
    success_url = reverse_lazy('Home Page')
    login_url = reverse_lazy("staff:login")
    context_object_name = 'publisher_delete'
    success_message = "Издатель был успешно удален!"
    permission_required = ('directories.delete_publisher')
  
     


