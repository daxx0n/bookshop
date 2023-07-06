from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django import forms
from . import models
from . import forms
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .models import Books
from django.shortcuts import redirect

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

@login_required(login_url='staff:login')
def add_comment(request, comment_id):
    form = CommentForm()
    books = get_object_or_404(Books, pk=comment_id)
    user = request.user

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.book = books
            comment.save()
            return redirect('books:book_view', books.pk)

    context = {'form': form}

    return render(request, 'comment_form.html', context)
