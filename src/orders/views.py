from typing import Any, Dict, Optional
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, FormView, TemplateView
from books.models import Books
from django.urls import reverse_lazy
from . import models, forms

# Create your views here.

class CartDetailView(DetailView):
    template_name = "orders/cart.html"
    model = models.Cart
    
    def get_object (self, *args, **kwargs):
        cart_pk = self.request.session.get("cart_id")
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_pk,
            defaults={
                "customer":customer
            }           
        )
        good_id = self.request.GET.get("good_id")
        quantity= self.request.GET.get("quantity")
        if good_id and quantity:
            quantity = int(quantity)
            good = Books.objects.get (pk=int(good_id))
            price = good.book_price
            good_in_cart, good_in_cart_created = models.GoodInCart.objects.get_or_create(
                cart = cart,
                good = good,
                defaults= {
                    "quantity":quantity,
                    "price":price * quantity
                }
            )
            if not good_in_cart_created:
                good_in_cart.quantity = good_in_cart.quantity + quantity
                good_in_cart.price = good_in_cart.price + price*quantity
                good_in_cart.save() 
            if created:
                self.request.session['cart_id'] = cart.pk
        return cart 
    
class CartAddDeleteItemView(DetailView):
    template_name = "orders/cart.html"
    model = models.Cart
    
    def get_object (self, *args, **kwargs):
        cart_pk = self.request.session.get("cart_id")
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_pk,
            defaults={
                "customer":customer
            }           
        )
        good_id = self.request.GET.get("good")
        action= self.request.GET.get("action")
        if good_id and action and action in ['add', 'delete']:
            good = Books.objects.get (pk=int(good_id))
            price = good.book_price
            good_in_cart = get_object_or_404(
                models.GoodInCart, 
                cart = cart,
                good = good,
            )
            if action == "add":
                addiction = 1
            else:
                if good_in_cart.quantity <= 1:
                    good_in_cart.delete()
                    return cart
                addiction = -1
            good_in_cart.quantity = good_in_cart.quantity + addiction
            good_in_cart.price = good_in_cart.quantity * price
            good_in_cart.save()
            
        return cart 
    
class CreateOrder (FormView):    
    form_class = forms.CreateOrderForm
    template_name = "orders/create_order.html"
    success_url = reverse_lazy("orders:complete-order")
    
    def form_valid(self, form):
        delivery_address = form.cleaned_data.get("delivery_address")
        status = models.Order(pk=1)
        cart_pk = int(self.request.session.get("cart_id"))
        cart = get_object_or_404(
            models.Cart,
            pk=cart_pk
        )
        obj = models.Order.objects.create(
            delivery_address = delivery_address,
            status = status,
            cart = cart
        )
        
        del self.request.session["cart_id"]
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", -100)
        context['object'] = get_object_or_404(
            models.Cart,
            pk=int(cart_id)
        )
        return context
    
class OrderSuccess(TemplateView):
    template_name = "orders/order-complete.html"