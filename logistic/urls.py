from django.urls import path
from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, sample_viev

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("stocks", StockViewSet)

urlpatterns = router.urls + [
    path("test/", sample_viev, name="test"),
]
