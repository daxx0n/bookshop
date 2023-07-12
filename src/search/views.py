from django.shortcuts import render
from django.views.generic import FormView 
from books import models
from directories import models as models_d
from django.db.models import Q
# Create your views here.

def search_view (request):
    res = []
    q = None
    if request.method == 'POST':
        q = request.POST.get("q")
        books = models.Books.objects.filter(Q(book_name__icontains=q))
        authors = models_d.Author.objects.filter(Q(author_lastname__icontains=q))
        genres = models_d.Genre.objects.filter(Q(genre_name__icontains=q))
        series = models_d.Serie.objects.filter(Q(serie_name__icontains=q))
        publishers = models_d.Publisher.objects.filter(Q(publisher_name__icontains=q))
        
        for obj in books:
            res.append((obj.book_name, obj.get_search_url_books()))
        for obj in authors:
            res.append(((obj.author_firstname + " " + obj.author_lastname), obj.get_search_url_author()))
        for obj in genres:
            res.append((obj.genre_name, obj.get_search_url_genre()))
        for obj in series:
            res.append((obj.serie_name, obj.get_search_url_serie()))
        for obj in publishers:
            res.append((obj.publisher_name, obj.get_search_url_publisher()))
    context = {"results":res, "q":q}
    return render (
        request, 
        template_name= 'search/search_results.html', 
        context=context)