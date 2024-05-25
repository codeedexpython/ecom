from django.urls import path
from fvtstore_app import views

urlpatterns = [
    path('',views.view_fvtstore),
    path('get/<int:store_id>/',views.get_view_store),
    path('create',views.add_store),
    path('update/<int:store_id>',views.update_store),
    path('delete/<int:store_id>',views.delete_store)
]
