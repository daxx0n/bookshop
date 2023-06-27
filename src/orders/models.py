from django.db import models
from django.contrib.auth import get_user_model
from books import models as bmodels

# Create your models here.

User = get_user_model()

class Cart (models.Model):
    customer = models.ForeignKey(
        User,
        verbose_name = "customer",
        on_delete = models.PROTECT,
        related_name = "carts",
        null = True,
        blank= True
    )

class GoodInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Cart',
        on_delete=models.CASCADE,
        related_name='goods'
    )   
    
    good = models.ForeignKey(
        bmodels.Books,
        verbose_name= "Good",
        on_delete = models.PROTECT
    )
    
    quantity = models.PositiveIntegerField(
        verbose_name='quantity',
        default=1
    )
    
    price = models.DecimalField(
        verbose_name= 'Price',
        max_digits=6,
        decimal_places=0
    )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name='updated',
        auto_now_add=False,
        auto_now=True
    )
    def __str__(self) -> str:
        return f"{self.good.name} x {self.quantity}"

class Order (models.Model):
    delivery_adress = models.OneToOneField(
        verbose_name = "Delivery adress"
    )
    status = models.ForeignKey(
        pass
    )
    cart = models.ForeignKey(
        Cart
        verbose_name="Cart",
    )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name='updated',
        auto_now_add=False,
        auto_now=True        
    )
