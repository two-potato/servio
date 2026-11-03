# Servio — focused engineering backlog

Updated: 2026-11-03. Scope: **only unresolved, verifiable work**. This list supersedes the old unstructured `todo`; completed task transcripts stay in Git history, not in the active backlog.

## P0 — make the repository demonstrably reliable

- [ ] **CI:** rerun `Backend Tests + Coverage` on the latest commit and fix every failure; keep `Security Audit` passing. The 2026-08-26 run failed during pytest startup due to duplicate Prometheus metric registration. A shared observability module and a regression test are included in the portfolio cleanup, but fresh green CI evidence is still required.
- [ ] **Recommendation feedback:** trace browser impression → click → API ingestion → persistent event → downstream feedback/analytics. Add an integration test that fails if clicks are only logged client-side or are ignored by the backend.
- [ ] **Authentication:** verify `/api/users/me/` and buyer account endpoints with session/JWT flows, including 401 handling and return URLs, on the Next.js frontend.
- [ ] **Public-repo hygiene:** audit tracked files and Git history for credentials, infrastructure identifiers and personal data; rotate any exposed secrets, then remove/privatize sensitive operational details. `.gitignore` does not erase history.
- [ ] **Portfolio verification:** smoke-test the documented fresh-clone Compose setup, Swagger endpoint, frontend build and critical purchase path. Record reproducible output and screenshots only from actual runs.

- [ ] **Branch consolidation:** after green CI, promote the reviewed candidate into the canonical `main` branch, make `main` the GitHub default and retire `dev`/candidate/release branches. Review the five unique `ref` commits before deletion; move the unrelated Sparts architecture spec from PR #5 to its own project before removing that branch. Do not bypass branch protection or the open draft production gate.

## P1 — close product migration gaps

- [ ] **Next.js buyer journeys:** confirm catalog → product → cart → checkout → order history on the new storefront; eliminate unneeded legacy redirects only after parity tests pass.
- [ ] **FastAPI extraction:** validate search/recommendation parity against the Django implementation, shadow/canary gates and rollback. Do **not** mark the migration complete just because service skeletons exist.
- [ ] **API contracts:** generate and validate OpenAPI schema; add contract checks for catalog, order, corporate-account and search/recommendation endpoints.
- [ ] **Observability:** define clear success/error/latency SLOs and useful dashboards for authentication, checkout, search and feedback.

## P2 — portfolio polish, after P0/P1

- [ ] Add authentic screenshots or a short screen recording of a working local demo, with test data and no sensitive identifiers.
- [ ] Consolidate old design/agent execution notes into a separately labelled historical archive **after** checking inbound links and active runbooks.

## Not in scope

Courier/PVZ/warehouse role expansion, badges for comments, 1C integrations and speculative near-Amazon features are **not** current commitments. Reintroduce them only with a validated use case and acceptance criteria.

**Rule:** each completed item needs a code/PR link and reproducible verification. Do not label untested work “done”.
