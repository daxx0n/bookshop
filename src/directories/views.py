from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.

def view_Author(request, pk):
    print (pk)
    author = models.Author.objects.get(pk=int(pk))
    html = f"Author PK:{author.pk} Author name {author.name}"
    return HttpResponse(html)
    