# Assignment from Baseball Operations Analytics

## Background

Our baseball operations analytics group wants to compare Tigers minor-league hitters with league peers. Before making comparisons, we need to understand the completeness, consistency, identifiers and statistical context of the available records. An attractive chart built on a mistaken join is a decision risk.

This is a small learning assignment, not access to a club's private scouting system or a predictive talent evaluation.

## Scope and questions

**Project: Tigers Double-A Data Quality and Peer Context Assessment.**

Use **2025 Erie SeaWolves batting records**, **2025 Eastern League batting records**, and **Erie player biographies** from the MLB Stats API. Start with an authorized mentor-prepared local snapshot so obtaining data does not become your first obstacle. Later reproduce the acquisition requests if time permits.

Answer:

1. How complete and plausible are player identifiers, reported season ages, playing opportunities and batting fields?
2. What does one row represent in each table, and do the proposed keys match that grain?
3. What happens when Erie records join to league records and biographies? Are there unmatched records or unexpected row multiplication?
4. How do workload, age definitions, rehab players and multi-team aggregates affect fair peer comparisons?
5. What should baseball operations verify or flag before relying on the data?

Define and document playing-time and age comparison rules before interpreting charts. One season supports descriptive peer context, not player improvement or future potential. Do not analyze signing bonuses or infer international signing eligibility. FanGraphs is an optional later project, not a prerequisite for this assignment.

## Required deliverables

| Deliverable | Minimum expectation |
|---|---|
| Python | Readable loading/validation scripts, explicit source paths, useful errors; no hidden notebook state |
| SQL | At least three saved .sql files addressing distinct audit questions; state each table's grain |
| Visualizations | Two meaningful, labelled charts answering different questions; include population, year and sample size |
| Dictionary | Source names/types/meaning, missing conventions, grain and keys; distinguish verified definitions from assumptions |
| Report | 600–900 words: population, methods, evidence, limitations and three prioritized actions |
| Reproducible repository | Exact dependency pins, run instructions, provenance manifest, tests Henry writes, safe public contents |
| Presentation | Five minutes: problem, trustworthy population, two findings and recommendations; about five slides |

The deliverable is code plus an auditable argument. A small static table or notebook is enough; a dashboard is not required. Real data should remain local unless its sharing rights are established. Explain how an authorized reviewer obtains inputs without bundling restricted content.

## Acceptance criteria

- Every input has a source URL, acquisition time in UTC, parameters and a file hash. Separate acquisition time from the performance season.
- Identify the grain before proposing a primary key. Count rows and distinct nonmissing player IDs separately; report missing IDs too.
- Missingness metrics state numerator and denominator, scope and units. Empty strings and absent columns are distinguished from observed numeric zero; all-missing or empty groups are handled explicitly.
- Duplicate checks distinguish identical rows, repeated player IDs at a legitimate grain and semantic duplicates. Do not delete records without a documented rule and preserved raw input.
- Joins use defensible IDs, declared expected cardinality and before/after row counts. Report unmatched records and missing keys; never silently match names or null IDs.
- At least one validation addresses schema, one missing/invalid values, and one key/join integrity. Add small tests that fail for the problem each check intends to catch.
- Three SQL queries have explanations, use correct NULL handling and denominators, and reconcile with a Python check on a selected result.
- Charts distinguish missing data from zero, show relevant sample sizes and avoid unsupported population, currency or causal labels.
- Document source years, rehabilitation players, team aggregation, season-age conventions, opportunity thresholds and unadjusted rate limitations.
- Finish with three actions tied to observed evidence, an owner and a verification step. The report separates observations from explanations/hypotheses.
- An authorized reviewer can run the documented pipeline from an empty processed-data directory. Review Git contents for sensitive or copyrighted outputs before public release.

## Exclusions and stop conditions

No machine learning, player valuation, causal inference, market-wide spending totals, all-signee MLB success probabilities, injury diagnosis, career projection or complex dashboard infrastructure. Do not spend time repairing an entire historical dataset. Log unresolved issues and bound the claims.

Access denial or uncertain permitted use is a real source blocker. Stop that acquisition; do not bypass protections or invent observations. Continue programming exercises while the mentor resolves the route, and ask the mentor for the authorized local snapshot; do not silently substitute teaching data.
