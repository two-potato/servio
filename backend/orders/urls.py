from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrderApproveView, OrderRejectView, OrderViewSet

router = DefaultRouter()
router.register("", OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>/approve/", OrderApproveView.as_view()),
    path("<int:pk>/reject/",  OrderRejectView.as_view()),
]
