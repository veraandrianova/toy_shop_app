from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('add_pay/', views.add_pay, name='add_pay'),
]
