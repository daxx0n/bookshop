from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.
# Home page

def home_page(request):
    authors = models.Author.objects.all()
    return render (
        request, 
        template_name="home_page.html", 
        context={'objects':authors})

# Read_object

def view_Author(request, pk):
    author = models.Author.objects.get(pk=int(pk))
    return render (
        request, 
        template_name="view_authors.html", 
        context={'object':author})

def view_Serie(request, pk):
    serie = models.Serie.objects.get(pk=int(pk))
    return render (
        request, 
        template_name="view_series.html", 
        context={'object':serie})


def view_Genre(request, pk):
    genre = models.Genre.objects.get(pk=int(pk))
    return render (
        request, 
        template_name="view_genres.html", 
        context={'object':genre})


def view_Publisher(request, pk):
    publisher = models.Publisher.objects.get(pk=int(pk))
    return render (
        request, 
        template_name="view_publishers.html", 
        context={'object':publisher})


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