# BYO textbooks (IITR commercial titles)

Commercial PDFs stay on **your** machine. This repo never wants those files in git.

## Drop folder

```text
.electrical-engineer/corpus/<book_id>/chapter-03.pdf
```

`EE_CORPUS_DIR` in `.env.example` points at `.electrical-engineer/corpus`. The directory is gitignored.

## Tag and ingest

```text
electrical-engineer rag add .electrical-engineer/corpus/hayt-circuits/ch3.pdf \
  --book-id hayt-circuits --chapter-id 3 --domain-tag circuits --licence-tag commercial-byo
electrical-engineer rag list
```

Then `electrical-engineer run explain-circuits` with a `problem.json` that sets `filters.book_id` and `query`.

## Still needed (catalog `byo_status: needed`)

From [`research/notes/iitr-ee-book-catalog.md`](../research/notes/iitr-ee-book-catalog.md):

- EEC-206 Electrical Machines — Fitzgerald / Nagrath–Kothari / Chapman
- EEC-208 Power Systems-I — Grainger / Weedy / Nagrath–Kothari
- EEC-301 Power Systems-II — Grainger / Glover / Saadat
- EEC-303 Power Electronics — Mohan / Rashid / Dubey
- EEL-302 Electric Drives — Dubey / Bose

Optional (OER already seeded for circuits): Hayt, Ogata, Oppenheim, Sedra, Sawhney, Hayt & Buck — add if you have the campus PDF.

Do not download from pirate hosts. Use your IITR library / publisher access.
