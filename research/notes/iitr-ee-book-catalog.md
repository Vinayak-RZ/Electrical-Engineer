# IIT Roorkee B.Tech EE — book catalog

**Role:** Maps IITR Electrical Engineering **program cores** to textbooks for BYO RAG. Not an indexable corpus and not a licence to redistributie commercial PDFs.  
**Date retrieved:** 2026-09-11  
**Programme:** B.Tech. Electrical Engineering, program code 115.

## How to use

Each core row has:

- `licence_tag: commercial-byo` — IITR-listed or campus-typical commercial text. Drop the PDF you have rights to under `.electrical-engineer/corpus/` (gitignored).
- `licence_tag: CC-BY` / `CC-BY-SA` / `owner-free` — author-intended free text; ingest from the owner URL.
- `licence_tag: CC-BY-NC` — free to read, **not** bundled in this Apache-2.0 repo.
- `byo_status: needed` — no SPDX-clean stand-in in git; you add the PDF.
- `byo_status: optional` — OER stand-in can be ingested; commercial text still useful if you have it.

Pirate hosts are not sources. PID/PRD: no commercial book bytes in git.

## Sources (dated)

| Source | URL | Retrieved | Notes |
|--------|-----|-----------|-------|
| IITR EE Programmes | https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/Academics/Programmes.html | 2026-09-11 | UG + M.Tech specialisations |
| Structure (NEP) | https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/static/Academics/Structure/UG/Structure_B.Tech_EE_NEP.pdf | 2026-09-11 | EEC-* PCC list |
| Acad NEP structure | https://acad.iitr.ac.in/Varsity/Academic_Programmes/UG_New/EE/Structure.pdf | 2026-09-11 | TLS cert expired; fetched with public URL |
| Structure (pre-NEP) | https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/static/Academics/Structure/UG/5.pdf | 2026-09-11 | EEN-* codes |
| UG syllabus (mod 09 Oct 2022) | https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/static/Academics/Syllabus/UG/UG_EE_Syllabus_mod_09oct22.pdf | 2026-09-11 | “11. Suggested Books” |
| Acad course outlines | https://acad.iitr.ac.in/Varsity/Academic_Programmes/UG_2024/COURSE%20OUTLINES%20OF%20EE.pdf | 2026-09-11 | Mostly later EE outlines |

NEP PCC titles come from the 2023–24 structure PDF. Suggested books come from the 2022 EEN syllabus (same department; codes renamed EEC-* in NEP). Where a NEP course has no matching EEN book list, the row says so.

## NEP program cores (PCC)

Institute-core maths/physics/HSS and programming (`EEC-101`, `CSE-101`) are out of the EE RAG pack map.

### EEC-102 Basic Electrical Science

- pack: circuits
- nep_code: EEC-102
- legacy_code: EEN-101 (Introduction to Electrical Engineering — partial overlap)
- licence_tag: commercial-byo
- iitr_listed:
  - Beaty / Fink, *Standard Handbook for Electrical Engineers* — licence_tag: commercial-byo
  - Singh S.N., *Electric Power Generation, Transmission and Distribution* — licence_tag: commercial-byo
- oer_standin:
  - Kuphaldt, *Lessons in Electric Circuits* Vol I (DC) — licence_tag: CC-BY — http://www.ibiblio.org/kuphaldt/electricCircuits/
- byo_status: optional

### EEC-104 Signals and Systems

- pack: signals
- nep_code: EEC-104
- legacy_code: EEN-356 (Signals and System, PEC in 2022 structure; NEP makes it PCC)
- licence_tag: commercial-byo
- iitr_listed:
  - Oppenheim, Willsky, Nawab, *Signals and Systems* — licence_tag: commercial-byo
  - Haykin / Van Veen, *Signals and Systems*, 2nd ed. — licence_tag: commercial-byo
- oer_standin:
  - Don Johnson, *Fundamentals of Electrical Engineering I* — licence_tag: CC-BY — https://open.umn.edu/opentextbooks/textbooks/fundamentals-of-electrical-engineering-1
- byo_status: optional

### EEC-201 Network Theory

- pack: circuits
- nep_code: EEC-201
- legacy_code: EEN-102
- licence_tag: commercial-byo
- iitr_listed:
  - Hayt, Kemmerly, Durbin, *Engineering Circuit Analysis* — licence_tag: commercial-byo
  - Van Valkenburg, *Network Analysis*, 3rd ed. — licence_tag: commercial-byo
  - Desoer / Kuh, *Basic Circuit Theory* — licence_tag: commercial-byo
  - Kuo F.F., *Network Analysis and Synthesis* — licence_tag: commercial-byo
- oer_standin:
  - Kuphaldt, *Lessons in Electric Circuits* Vol I–II — licence_tag: CC-BY — http://www.ibiblio.org/kuphaldt/electricCircuits/
- byo_status: optional

### EEC-202 Electrical and Electronic Measurements

- pack: measurements
- nep_code: EEC-202
- legacy_code: EEN-104
- licence_tag: commercial-byo
- iitr_listed:
  - Golding / Widdis, *Electrical Measurements and Measuring Instruments* — licence_tag: commercial-byo
  - Harris F.K., *Electrical Measurements* — licence_tag: commercial-byo
  - Doebelin, *Measurement Systems* — licence_tag: commercial-byo
- oer_standin:
  - Kuphaldt, *Lessons in Industrial Instrumentation* / ModEL — licence_tag: CC-BY — https://ibiblio.org/kuphaldt/socratic/model/index.html
- byo_status: optional

### EEC-204 Control Systems

- pack: control
- nep_code: EEC-204
- legacy_code: EEN-211
- licence_tag: commercial-byo
- iitr_listed:
  - Nagrath / Gopal, *Control System Engineering*, 5th ed. — licence_tag: commercial-byo
  - Ogata, *Modern Control Engineering* — licence_tag: commercial-byo
  - Dorf / Bishop, *Modern Control Systems* — licence_tag: commercial-byo
  - Nise (Norman S. N.), *Control Systems Engineering* — licence_tag: commercial-byo
  - Kuo B.C., *Automatic Control Systems* — licence_tag: commercial-byo
- oer_standin:
  - Åström / Murray, *Feedback Systems* — licence_tag: owner-free — https://fbswiki.org/wiki/index.php/FBS (Princeton keeps print rights; authors host a free web PDF)
- byo_status: optional

### EEC-206 Electrical Machines

- pack: machines
- nep_code: EEC-206
- legacy_code: EEN-201 + EEN-202
- licence_tag: commercial-byo
- iitr_listed:
  - Fitzgerald, Kingsley, Kusko, *Electric Machinery* — licence_tag: commercial-byo
  - Nagrath / Kothari, *Electrical Machines* — licence_tag: commercial-byo
  - Chapman, *Electric Machinery Fundamentals* — licence_tag: commercial-byo
  - Say M.G., *The Performance and Design of Alternating Current Machines* — licence_tag: commercial-byo
- oer_standin: none SPDX-clean at retrieve date
- byo_status: needed

### EEC-208 Power Systems-I

- pack: power
- nep_code: EEC-208
- legacy_code: EEN-206 (Power Transmission and Distribution)
- licence_tag: commercial-byo
- iitr_listed:
  - Weedy / Cory, *Electric Power Systems* — licence_tag: commercial-byo
  - Grainger / Stevenson, *Elements of Power System Analysis* — licence_tag: commercial-byo
  - Nagrath / Kothari, *Modern Power System Analysis* — licence_tag: commercial-byo
- oer_standin: none SPDX-clean at retrieve date (Preetham power notes: verify CC-BY before ingest)
- byo_status: needed

### EEC-301 Power Systems-II

- pack: power
- nep_code: EEC-301
- legacy_code: EEN-301 (Power System Analysis and Control)
- licence_tag: commercial-byo
- iitr_listed:
  - Grainger / Stevenson, *Power System Analysis* — licence_tag: commercial-byo
  - Glover / Sarma, *Power System Analysis and Design* — licence_tag: commercial-byo
  - Saadat, *Power System Analysis* — licence_tag: commercial-byo
  - Kothari / Nagrath, *Modern Power System Analysis* — licence_tag: commercial-byo
- oer_standin: none SPDX-clean at retrieve date
- byo_status: needed

### EEC-303 Power Electronics

- pack: power_electronics
- nep_code: EEC-303
- legacy_code: EEN-303
- licence_tag: commercial-byo
- iitr_listed:
  - Mohan, Undeland, Robbins, *Power Electronics* — licence_tag: commercial-byo
  - Rashid, *Power Electronics Circuits, Devices and Applications* — licence_tag: commercial-byo
  - Dubey / Doradla / Joshi / Sinha, *Thyristorised Power Controllers* — licence_tag: commercial-byo
- oer_standin: none SPDX-clean at retrieve date
- byo_status: needed

### ECE-101 Fundamentals of Electronics / ECE-103 Digital Electronics

- pack: electronics
- nep_code: ECE-101, ECE-103 (ESC; taught with EE)
- legacy_code: EEN-106 Analog Electronics; EEN-203 Digital Electronics and Circuits
- licence_tag: commercial-byo
- iitr_listed:
  - Boylestad / Nashelsky, *Electronic Devices and Circuit Theory* — licence_tag: commercial-byo
  - Franco, *Design with Operational Amplifiers and Analog Integrated Circuits* — licence_tag: commercial-byo
  - Mano / Ciletti, *Digital Design* — licence_tag: commercial-byo
  - Malvino / Leach, *Digital Principles and Applications* — licence_tag: commercial-byo
- oer_standin:
  - Kuphaldt, *Lessons in Electric Circuits* Vol III (Semiconductors) and Vol IV (Digital) — licence_tag: CC-BY
- byo_status: optional

### PHN-003 / Physics EM (institute BSC; NEP uses PHI-101)

- pack: em
- nep_code: PHI-101 Physics-I (EM topics may sit here; pre-NEP PHN-003 Electromagnetic Field Theory)
- licence_tag: commercial-byo
- iitr_listed:
  - Hayt / Buck, *Engineering Electromagnetics* — licence_tag: commercial-byo
  - Sadiku, *Elements of Engineering Electromagnetics* — licence_tag: commercial-byo
- oer_standin:
  - Ellingson, *Electromagnetics* Vol 1 (Virginia Tech) — licence_tag: CC-BY-SA
- byo_status: optional

### EEL-302 Electric Drives (PEC; NEP list)

- pack: power_electronics
- nep_code: EEL-302
- legacy_code: EEN-302
- licence_tag: commercial-byo
- iitr_listed:
  - Dubey, *Fundamentals of Electric Drives* — licence_tag: commercial-byo
  - Bose, *Power Electronics and Variable Frequency Drives* — licence_tag: commercial-byo
  - Pillai, *A First Course in Electric Drives* — licence_tag: commercial-byo
- oer_standin: none SPDX-clean at retrieve date
- byo_status: needed

### EEN-355 Digital Signal Processing (PEC)

- pack: signals
- nep_code: EEL-355
- legacy_code: EEN-355
- licence_tag: commercial-byo
- iitr_listed:
  - Mitra, *Digital Signal Processing: A Computer-Based Approach* — licence_tag: commercial-byo
  - Oppenheim / Schafer / Buck, *Discrete-Time Signal Processing* — licence_tag: commercial-byo
  - Haykin / Van Veen, *Signals and Systems* — licence_tag: commercial-byo
- oer_standin:
  - Smith S.W., *The Scientist and Engineer’s Guide to Digital Signal Processing* — licence_tag: owner-free — https://www.dspguide.com (record the site grant before bundling)
- byo_status: optional

## Also named on IITR EE programme page (not separate PCC)

Drives, power electronics, power systems, control, instrumentation, signal processing — covered by the PCC/PEC rows above. M.Tech structures (ISP, EDPE, PSE, S&C, EVT) are **out of the UG public promise**; do not ingest PG-only books as v1 cores.

## NC / do-not-bundle

- Fiore DC/AC circuit texts — often CC-BY-NC
- Adams, *Signals and Systems* — BY-NC-ND
- Ellingson, *Radio Systems Engineering* — CC-BY-NC

Link or BYO locally. Do not ship in git.

## BYO drop folder

```text
.electrical-engineer/corpus/<book_id>/<chapter>.pdf
```

Gitignored. `electrical-engineer rag add` then `rag tag` with `book_id`, `chapter_id`, `domain_tag`, `licence_tag`.

## Gaps (you add)

`byo_status: needed` today: machines (EEC-206), power (EEC-208, EEC-301), power electronics (EEC-303), drives (EEL-302).
