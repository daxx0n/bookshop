from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Books
from . import models
from . import forms

# Create your views here.

class BookListView (generic.ListView):
    template_name = "book_list.html"
    model = models.Books
    paginate_by = 10

class BookView (generic.DetailView):
    template_name = "view_book.html"
    model = models.Books

class BookCreateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Books
    form_class = forms.BookModelForm
    template_name = "add.html"
    login_url = reverse_lazy("staff:login")
    context_object_name = 'book_create'
    success_url = reverse_lazy('Home Page')
    success_message = 'Книга была успешно создана!'
    permission_required = "books.add_books"
     
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()


class BookUpdateView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Books
    form_class = forms.BookModelForm
    template_name = "update.html"
    login_url = reverse_lazy("staff:login")
    context_object_name = 'book_update'
    success_url = reverse_lazy('Home Page')
    success_message = 'Книга была успешно обновлена!'
    permission_required = "books.change_books"

    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()
   
class BookDeleteView (LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, generic.DeleteView, ):
    model = models.Books
    template_name = "delete_book.html"
    login_url = reverse_lazy("staff:login")
    context_object_name = 'book_delete'
    success_url = reverse_lazy('Home Page')
    success_message = 'Книга была успешно удалена!'
    permission_required = "books.delete_books"

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
