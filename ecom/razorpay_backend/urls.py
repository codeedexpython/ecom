from django.urls import path
from .views import *

urlpatterns = [
    path('order/create/',CreateOderAPIview.as_view(),name='online_payment_create'),
    path('order/complete/',TransactionAPIView.as_view(),name='online_payment_complete'),
]