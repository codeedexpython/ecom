"""
URL configuration for order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from order_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.view_order),
    path('add',views.add_order),
    path('get/<int:order_id>',views.get_view_order),
    path('update/<int:order_id>',views.update_order),
    path('delete/<int:order_id>',views.delete_order),
    path('total_orders',views.total_order),
    path('total_pending',views.total_pending_order),
    path('search',views.search_order),
    path('total_completed',views.total_completed_order),
    path('total_failed',views.total_failed_order),
    path('total_unfulfilled',views.total_unfulfilled_order),
    path('fetch/<int:customer_id>',views.fetch_customer_orders)
]

