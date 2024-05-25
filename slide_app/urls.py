from django.urls import path
from slide_app import views

urlpatterns = [
    path('',views.carousel_slide_list),
    path('get/<int:id>/',views.carousel_slide_get),
    path('create',views.carousel_slide_create),
    path('update/<int:id>',views.carousel_slide_update),
    path('delete/<int:id>',views.carousel_slide_delete)
]
