from django import forms
from .models import Order

class CreateOrderForm(forms.Form):
    delivery_address = forms.CharField(
        required=True, 
        widget=forms.Textarea
    )
    phone = forms.CharField(
        required=True
    )
    