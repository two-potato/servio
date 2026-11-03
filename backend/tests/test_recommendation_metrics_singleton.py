"""Regression: both import paths must reuse the same Prometheus collectors."""

from recommendation_api import observability as public_observability
from shopfront.recommendation import observability as shopfront_observability


def test_recommendation_metrics_are_registered_only_once():
    for name in (
        "RECOMMENDATION_SELECTIONS_TOTAL",
        "RECOMMENDATION_CANDIDATE_COUNT",
        "RECOMMENDATION_EVENTS_TOTAL",
        "RECOMMENDATION_ATTRIBUTED_ORDERS_TOTAL",
        "RECOMMENDATION_ATTRIBUTED_REVENUE_TOTAL",
    ):
        assert getattr(shopfront_observability, name) is getattr(public_observability, name)
