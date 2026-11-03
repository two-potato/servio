"""Regression: search API and storefront must share Prometheus collectors."""

from search_api import observability as public_observability
from shopfront.searching import observability as shopfront_observability


def test_search_metrics_are_registered_only_once():
    for name in (
        "SEARCH_REQUESTS_TOTAL",
        "SEARCH_ZERO_RESULTS_TOTAL",
        "SEARCH_REWRITES_TOTAL",
        "SEARCH_LATENCY_SECONDS",
        "SEARCH_FEEDBACK_EVENTS_TOTAL",
        "SEARCH_ATTRIBUTED_ORDERS_TOTAL",
        "SEARCH_ATTRIBUTED_REVENUE_TOTAL",
    ):
        assert getattr(shopfront_observability, name) is getattr(public_observability, name)
