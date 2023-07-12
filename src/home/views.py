from django.views import generic
from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from books.models import Books


# Create your views here.

# Home page

class HomePage (generic.TemplateView):
    template_name = "home_page.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        books = Books.objects.all()
        context.update({
            "object_list": books
        })
        return context


def success_page(request):
    return render(
        request,
        template_name='book-shop/success.html'
    )