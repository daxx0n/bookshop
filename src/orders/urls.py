from django.urls import path
from . import views
app_name = 'orders'

urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name="view-cart"),
    path('cart-items-edit/', views.CartAddDeleteItemView.as_view(), name="cart-items-edit"),
    path('create-order/', views.CreateOrder.as_view(), name="create-order"),
    path('complete-order/', views.OrderSuccess.as_view(), name="complete-order"),
    path('orders-history/', views.history_order, name="history-order"),
]