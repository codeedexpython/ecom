from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductSizeViewSet


router = DefaultRouter()

router.register("products", ProductViewSet, basename='product')
router.register("product-sizes", ProductSizeViewSet, basename='productsize')

urlpatterns = [
    path('', include(router.urls)),
]