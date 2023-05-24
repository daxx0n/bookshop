from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.
# Home page

def home_page(request):
    authors = models.Author.objects.all()
    html = "<ul>"
    for author in authors:
        html += f"<li> {author.pk} Author {author.author_firstname} </li>"
    html += "<ul>"
    return render (request, template_name="home_page.html", context={})

# Read_object

def view_Author(request, pk):
    author = models.Author.objects.get(pk=int(pk))
    html = f"Author's PK:{author.pk}. Author's firstname and lastname: {author.author_firstname} {author.author_lastname}"
    return HttpResponse(html)

def view_Serie(request, pk):
    serie = models.Serie.objects.get(pk=int(pk))
    html = f"Serie PK:{serie.pk}. Serie name: {serie.serie_name}"
    return HttpResponse(html)

def view_Genre(request, pk):
    genre = models.Genre.objects.get(pk=int(pk))
    html = f"Genre PK:{genre.pk}. Genre name: {genre.genre_name}"
    return HttpResponse(html)

def view_Publisher(request, pk):
    publisher = models.Publisher.objects.get(pk=int(pk))
    html = f"Publisher's PK:{publisher.pk}. Publisher's name: {publisher.publisher_name}"
    return HttpResponse(html)

# Delete object

def delete_Publisher(request, pk):
    models.Publisher.objects.get(pk=int(pk)).delete()
    return HttpResponse(f"Publisher, id {pk} has been deleted!")

def delete_Author(request, pk):
    models.Author.objects.get(pk=int(pk)).delete()
    return HttpResponse(f"Author, id {pk} has been deleted!")

def delete_Serie(request, pk):
    models.Serie.objects.get(pk=int(pk)).delete()
    return HttpResponse(f"Serie, id {pk} has been deleted!")

def delete_Genre(request, pk):
    models.Genre.objects.get(pk=int(pk)).delete()
    return HttpResponse(f"Genre, id {pk} has been deleted!")