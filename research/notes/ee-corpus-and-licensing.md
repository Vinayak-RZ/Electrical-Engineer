# EE corpus candidates and licensing

## Purpose

Map which electrical-engineering textbooks and open resources could ground an EE agent, and which rights models are safe for an open-source project.

## Findings

Claim | Evidence (URL) | Confidence
--- | --- | ---
A redistributed commercial textbook PDF corpus is a **rights risk** for an OSS repo | general copyright practice; plan non-goal | high
**Bring-your-own-PDF (BYO)** at runtime plus optional OER packs is the licence-safe default | this note’s rights matrix | high
Curricula imply domain coverage (circuits, machines, power, control, power electronics, signals) even when specific editions vary by campus | https://static.collegedekho.com/media/uploads/2024/07/01/gate-_ee_2025_syllabus.pdf ; https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/Academics/Programmes.html | high

### Domain → canonical text *candidates* (titles only — not an indexable corpus claim)

| Domain | Example titles commonly used in undergrad EE (verify edition locally) |
|--------|------------------------------------------------------------------------|
| Electric circuits | Nilsson & Riedel; Hayt, Kemmerly & Durbin; Alexander & Sadiku |
| Electrical machines | Chapman; Fitzgerald, Kingsley & Umans; Sen |
| Power systems | Grainger & Stevenson; Glover, Overbye & Sarma; Nagrath & Kothari |
| Control systems | Nise; Ogata; Dorf & Bishop |
| Power electronics | Mohan, Undeland & Robbins; Rashid; Erickson & Maksimovic |
| Signals & systems | Oppenheim & Willsky; Lathi |
| EM fields | Hayt & Buck; Sadiku |

These are **pointers for a user’s private library**, not files this project will ship.

### Rights models

| Model | What the project stores | Redistribution | Fit |
|-------|-------------------------|----------------|-----|
| Owned PDFs committed to repo | Full text | Illegal for commercial books | **Reject** |
| Institute library scrape | Full text | Usually prohibited | **Reject** |
| OER / openly licensed texts | Allowed texts + licence file | OK if licence permits | **Optional pack** |
| **BYO-PDF at runtime** | Indexer code + user-local index | User keeps PDFs | **Default** |
| Citation-only knowledge (no PDF) | Metadata + public syllabi | OK | Complements BYO |

### OER seed candidates (ship only if redistribution licence is clear)

| Resource | Domain | Licence caution |
|----------|--------|-----------------|
| Kuphaldt ModEL modules | Power / electronics modules | **CC BY 4.0** — strongest OSS seed candidate ([ModEL](https://ibiblio.org/kuphaldt/socratic/model/index.html)) |
| Preetham *Introduction to power system engineering* | Power | Listed **CC BY** on OER Commons |
| Fiore DC/AC circuit texts | Circuits | Often **NC** (non-commercial) — **not** a default OSS-bundled corpus |
| Adams *Signals and Systems* | Signals | **BY-NC-ND** — free to read; not a redistributable OSS default |
| LibreTexts EE bookshelf | Mixed | Verify **per-page** licence before bundling |

**Rule:** bundled seed corpus must be commercially redistributable (e.g. CC BY / BY-SA / public domain). NC-licensed OER stays user-local or linked, not shipped in the repo.

### Stance (D3)

**Default: BYO-PDF + optional CC-BY (or equivalent) OER packs.** The agent ships ingestion/retrieval software and skill prompts. Users point it at PDFs they have rights to read. No commercial book bytes in git.

## Open questions

- Curate a minimal CC-BY seed list (ModEL + verified BY power notes) with SPDX metadata.
- User CP-1 may expand to “we own licences for X” — then a private index is fine, still not for public redistribution.

## Sources

- [GATE EE 2025 syllabus PDF](https://static.collegedekho.com/media/uploads/2024/07/01/gate-_ee_2025_syllabus.pdf) — retrieved 2026-09-07 — reliability: secondary (S11)
- [IIT Roorkee EE Programmes](https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/Academics/Programmes.html) — retrieved 2026-09-07 — reliability: primary (S12)
- [ETH Electric Energy Engineering](https://ethz.ch/content/dam/ethz/special-interest/itet/department/Studies/Electric_Energy_Engineering.pdf) — retrieved 2026-09-07 — reliability: primary (S13)
- [Kuphaldt ModEL](https://ibiblio.org/kuphaldt/socratic/model/index.html) — retrieved 2026-09-07 — reliability: primary
- [Open Source Definition §6](https://opensource.org/osd) — retrieved 2026-09-07 — reliability: primary
- Research plan non-goals (no book text in repo) — retrieved 2026-09-07 — reliability: primary

## Confidence

Overall confidence for this note: high

The licence-safe default does not depend on which edition a campus uses. Named OER seeds still need a short SPDX pass before any pack ships.
