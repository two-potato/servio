"""Compatibility import path for the shared search metrics.

Search metrics must be registered with Prometheus only once per Python process.
Both search_api and the legacy shopfront use the same collector instances.
"""

from search_api.observability import (
    SEARCH_ATTRIBUTED_ORDERS_TOTAL,
    SEARCH_ATTRIBUTED_REVENUE_TOTAL,
    SEARCH_FEEDBACK_EVENTS_TOTAL,
    SEARCH_LATENCY_SECONDS,
    SEARCH_REQUESTS_TOTAL,
    SEARCH_REWRITES_TOTAL,
    SEARCH_ZERO_RESULTS_TOTAL,
    observe_search_feedback_event,
    observe_search_order_attribution,
    observe_search_response,
    observe_search_rewrite,
)

__all__ = [
    "SEARCH_ATTRIBUTED_ORDERS_TOTAL",
    "SEARCH_ATTRIBUTED_REVENUE_TOTAL",
    "SEARCH_FEEDBACK_EVENTS_TOTAL",
    "SEARCH_LATENCY_SECONDS",
    "SEARCH_REQUESTS_TOTAL",
    "SEARCH_REWRITES_TOTAL",
    "SEARCH_ZERO_RESULTS_TOTAL",
    "observe_search_feedback_event",
    "observe_search_order_attribution",
    "observe_search_response",
    "observe_search_rewrite",
]
