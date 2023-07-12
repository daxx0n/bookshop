from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Cart)
admin.site.register(models.GoodInCart)
admin.site.register(models.Order)