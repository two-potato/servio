"""Compatibility shim: share the Prometheus metric objects registered by the API layer.

The old copy of this module declared the same metric names twice, which raised
prometheus_client.registry.DuplicateTimeseries during django.setup().
Keep this import path for existing shopfront callers without re-registering.
"""

from recommendation_api.observability import (
    RECOMMENDATION_ATTRIBUTED_ORDERS_TOTAL,
    RECOMMENDATION_ATTRIBUTED_REVENUE_TOTAL,
    RECOMMENDATION_CANDIDATE_COUNT,
    RECOMMENDATION_EVENTS_TOTAL,
    RECOMMENDATION_SELECTIONS_TOTAL,
    observe_recommendation_event,
    observe_recommendation_order_attribution,
    observe_recommendation_selection,
)

__all__ = [
    "RECOMMENDATION_ATTRIBUTED_ORDERS_TOTAL",
    "RECOMMENDATION_ATTRIBUTED_REVENUE_TOTAL",
    "RECOMMENDATION_CANDIDATE_COUNT",
    "RECOMMENDATION_EVENTS_TOTAL",
    "RECOMMENDATION_SELECTIONS_TOTAL",
    "observe_recommendation_event",
    "observe_recommendation_order_attribution",
    "observe_recommendation_selection",
]
