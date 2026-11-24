from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, CategoryViewSet, ProductViewSet, SeriesViewSet

router = DefaultRouter()
router.register("brands", BrandViewSet)
router.register("series", SeriesViewSet)
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)

urlpatterns = [ path("", include(router.urls)) ]
