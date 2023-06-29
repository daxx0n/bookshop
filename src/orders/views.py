from django.shortcuts import render
from django.views.generic import DetailView
from . import models

# Create your views here.

class Cart(DetailView):
    template_name = "orders/cart.html"
    model = models.Cart
