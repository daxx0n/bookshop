from django.shortcuts import render
from django.views.generic import FormView 
from books import models
from directories import models
from django.db.models import Q
# Create your views here.

def search_view (request):
    if request.method == 'POST':
        q = request.post.get("q")
        books = models.Books.objects.filter(Q(name__icontains=q))
        print (q)
        res = []
        for obj in books:
            res.append((obj.name, obj.get_search_url()))
    context = {}
    context ['search_results'] = []
    return render (request, template_name='search_results.html', context=context)