# Servio | Engineering case study

**Type:** personal portfolio / multi-vendor B2B commerce platform  
**Repository:** https://github.com/two-potato/servio  
**Status:** evolving prototype with substantial implemented modules and some incomplete migrations. No claim of a verified public deployment or production-scale traffic.

## The problem

Professional procurement often involves multiple suppliers, corporate purchasing entities, negotiated order flows, approvals and a catalog with complicated discovery requirements. Servio explores how to build these workflows in one extensible commerce platform while keeping the transactional core maintainable.

This is not a claim that the software is a finished Amazon competitor. It is an engineering demonstration of the domain model, service boundaries, integration points and delivery practices.

## Engineering scope supported by the code

**Domain and transactional backend.** Django/DRF modules model product catalogs, seller offers, company memberships, corporate workspaces, orders, order states and payments/checkout adapters. PostgreSQL remains the business system of record. Inspect `backend/catalog/`, `backend/commerce/`, `backend/orders/`, `backend/users/` and `backend/config/`.

**Storefront evolution.** The older user experience is Django templates + HTMX. The repository also has a Next.js/React storefront and Django bridge endpoints for buyer data. These coexist while migration continues; see `backend/shopfront/`, `backend/storefront_api/` and `frontend/`.

**Search and recommendation boundaries.** OpenSearch indexes and Django orchestration support discovery. FastAPI search/recommendation services are present as a contract-first extraction path with fallback/shadow principles. Their existence is **not** evidence of full parity, personalisation quality or production cutover. See `services/search-api/`, `services/recommendation-api/`, `backend/shopfront/searching/` and `backend/shopfront/recommendation/`.

**Async work and integrations.** Redis/Celery handle background operations; Telegram flows and outbound notifications are represented by `bot/` and task modules. Recommendation/order attribution processing provides an example of the complexity in measuring a marketplace journey.

**Engineering operations.** The repository includes CI, security-audit workflows, Docker development stacks, monitoring configurations and Swarm manifests. Deployment documents also contain references to a separate 24sparts experiment; those are operational context, not proof that Servio itself is running at a given URL.

## Design choices and trade-offs

| Decision | Rationale | Limitation / follow-up |
| --- | --- | --- |
| Django modular monolith for commerce | One transactional model for accounts, companies, orders and catalog | Thin views, service boundaries and regression tests are needed as features grow |
| Separate discovery APIs incrementally | Search and recommendations can evolve without splitting transactional consistency | Fallback, contracts, parity, real feedback events and canary tests are not optional |
| PostgreSQL + Redis + OpenSearch | Clear separation of records, async/cache and search projection | Reindexing, eventual consistency and degradation paths need test evidence |
| Keep HTMX during Next.js migration | Avoid replacing all buying journeys in one risky rewrite | Dual UI routes create maintenance cost until parity is established |
| Instrument recommendation journey | Measure whether suggested products lead to useful actions | Client-side clicks alone are not reliable feedback; verify ingestion and attribution |

## What to review in 10 minutes

1. Start with [the system diagram](ARCHITECTURE.md) and [backend layering guide](BACKEND_GUIDE.md).
2. Inspect [catalog models](../backend/catalog/models/) and [order domain](../backend/orders/).
3. Open [the Next.js storefront](../frontend/) beside [the legacy storefront](../backend/shopfront/).
4. Review [the API specification](../backend/API.md) and [FastAPI migration plan](API_PLATFORM_PLAN_FASTAPI_SEARCH_RECO_RU.md).
5. Review [GitHub Actions](https://github.com/two-potato/servio/actions) and [the focused backlog](../TODO.md), especially unresolved verification gates.

## Reproducibility

From a fresh clone, use the commands in [LOCAL_DEVELOPMENT.md](LOCAL_DEVELOPMENT.md). Useful reviewer checks include:

```bash
make test
make lint
cd frontend && npm ci && npm run typecheck && npm run build
```

The exact environment variables, ports and external service dependencies are documented in example environment files. These checks are **instructions**, not a statement that the current commit has passed them.

## Known gaps (do not oversell)

- The production candidate's 2026-08-26 CI failed at Django startup with duplicate Prometheus registration; the repair requires a fresh passing CI run.
- Recommendation click-to-feedback completeness must be demonstrated by an end-to-end regression test.
- The Next.js buyer flow and Django legacy storefront still overlap.
- FastAPI discovery contracts are transitional until parity and rollout evidence exist.
- Demo media, realistic test data, and neutralized public operations documentation need a separate proof pass.

## Next milestone

Make the latest candidate boringly reproducible: clean clone → build → test → demo transaction → captured CI evidence. Only then consider a production release or a portfolio claim of stability.
