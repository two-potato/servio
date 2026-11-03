# Servio — roadmap

> Portfolio-oriented project roadmap. This file describes **remaining work**, not promised or completed functionality. Last updated: 2026-11-03.

## Core engineering

- [ ] **Recommendation telemetry:** verify impression → click → API event → durable feedback → attribution and add an integration test covering the entire path.
- [ ] **Buyer account:** complete and verify the Next.js catalog, cart, checkout, order-history and authentication flows; remove legacy redirects only after functional parity.
- [ ] **Discovery services:** finish contract/parity validation for FastAPI search and recommendation adapters against the Django fallbacks. Preserve safe routing and rollback.
- [ ] **Dependencies:** update vulnerable frontend dependency versions and regenerate the npm lockfile using npm; retain a reproducible build and an accurate dependency manifest.

## Portfolio finish

- [ ] Add screenshots or a concise demo video recorded from a working local installation with synthetic catalog/order data.
- [ ] Document one repeatable local demonstration path: open catalog, search/filter, add to cart, check out, inspect order.
- [ ] Review the public repository for secrets, operational IP addresses, proprietary data and environment-specific instructions. Rotate anything previously exposed; removing a file does not erase Git history.
- [ ] Consolidate outdated UX experiments and historical execution transcripts into an archive without removing currently used architecture/runbook references.

## Deferred ideas (not committed scope)

- Courier, pickup-point and warehouse staff roles
- 1C / document-exchange integrations
- Gamification/rating of community comments
- Advanced personalized ranking before reliable event collection

The GitHub repository is a **technical portfolio**, not evidence of an operational e-commerce business or production deployment. Every future feature claim should point to implemented code and a reproducible example.
