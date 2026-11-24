from django.urls import path

from .views_admin import (
    ApproveEntityCreationView,
    ApproveMembershipView,
    RejectEntityCreationView,
    RejectMembershipView,
)

urlpatterns = [
    path("admin/membership-requests/<int:pk>/approve/", ApproveMembershipView.as_view()),
    path("admin/membership-requests/<int:pk>/reject/",  RejectMembershipView.as_view()),
    path("admin/entity-creation-requests/<int:pk>/approve/", ApproveEntityCreationView.as_view()),
    path("admin/entity-creation-requests/<int:pk>/reject/",  RejectEntityCreationView.as_view()),
]
