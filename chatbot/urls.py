from django.urls import path
from .views import *

urlpatterns = [
    path('message/<int:user_id>/', message_view, name='message_view'),
]