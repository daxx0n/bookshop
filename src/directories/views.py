from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.

def view_Author(request, pk):
    print (pk)
    author = models.Author.objects.get(pk=int(pk))
    html = f"Author PK:{author.author_firstname.pk} Author name {author.author_firstname.pk}"
    return HttpResponse(html)
    