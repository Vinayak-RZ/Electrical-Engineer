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

### Stance (D3)

**Default: BYO-PDF + optional OER packs.** The agent ships ingestion/retrieval software and skill prompts. Users point it at PDFs they have rights to read. No commercial book bytes in git.

## Open questions

- Which specific OER EE texts are high enough quality for undergrad cores (needs a later survey pass)?
- User CP-1 may expand to “we own licences for X” — then a private index is fine, still not for public redistribution.

## Sources

- [GATE EE 2025 syllabus PDF](https://static.collegedekho.com/media/uploads/2024/07/01/gate-_ee_2025_syllabus.pdf) — retrieved 2026-09-07 — reliability: secondary (S11)
- [IIT Roorkee EE Programmes](https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/Academics/Programmes.html) — retrieved 2026-09-07 — reliability: primary (S12)
- [ETH Electric Energy Engineering](https://ethz.ch/content/dam/ethz/special-interest/itet/department/Studies/Electric_Energy_Engineering.pdf) — retrieved 2026-09-07 — reliability: primary (S13)
- Research plan non-goals (no book text in repo) — retrieved 2026-09-07 — reliability: primary

## Confidence

Overall confidence for this note: high

The licence-safe default does not depend on which edition a campus uses. OER quality survey remains medium-confidence unfinished work for a later spike, not a blocker for the recommendation.
