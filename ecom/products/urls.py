from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register("products", ProductViewSet, basename='product')
router.register("product/sizes", ProductSizeViewSet, basename='productsize')

urlpatterns = [
    path('', include(router.urls)),
    path('customer/refund/orders/<int:customer_id>/', CustomerRefundProductDetailsAPIView.as_view(), name='customer_refund_product_details'),
]