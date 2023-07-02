from django.forms import ModelForm
from . import models

class CreateOrderForm(ModelForm):
    class Meta:
        model = models.Order
        fields = (
            'delivery_adress',
        )