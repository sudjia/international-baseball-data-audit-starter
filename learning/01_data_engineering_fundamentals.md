# 1. Data engineering fundamentals

## Why it matters

Think of a data pipeline as a laboratory protocol: the results are trustworthy only if inputs, instruments, processing steps and assumptions are traceable. A plot is the final measurement display, not the entire experiment.

## Simple explanation

A **pipeline** is an ordered, repeatable set of steps from source to usable output. **Ingestion** obtains data; **transformation** changes representation or computes fields; **storage** keeps the artifacts for later use. A **schema** describes columns, types, grain and constraints.

**ETL** means extract, transform, load: clean before loading an analytical store. **ELT** loads first and transforms in the store. For this project, save raw JSON, load deliberately defined tables, then use pandas/SQL transformations. You need neither a warehouse service nor orchestration software.

Keep three layers: raw (original bytes), cleaned (typed values with documented rules), analytical (tables at the exact grain your question needs). A **batch** processes a bounded file/date snapshot rather than every event instantly. Your project is one small batch.

**Lineage** tells where a value/table came from and which steps produced it. **Provenance** records source URL, parameters, UTC acquisition time, file hash and source year. Reproducibility means a reviewer can repeat the documented steps, or understand why a changing source produces different results.

A one-off notebook can depend on cells run out of order. Production work also needs scheduling, monitoring, access control, recovery and contracts. Learn the habits—clear inputs/errors, logging and tests—without building that infrastructure here.

## Baseball example

A scout board and batting file refer to different years. Saving the retrieval time does not make those years equal. Preserve both, define the ID bridge, and record transformations before drawing any player comparison.

## Common mistakes

- Editing the raw file, then losing evidence of the original problem.
- Using today's date as the performance season.
- Treating an API response as a stable, complete dataset without checking it.
- Installing a database server when an in-process engine is sufficient.

## Recommended reading

[DuckDB Python overview](https://duckdb.org/docs/stable/clients/python/overview.html), optional orientation; required source-use reading is in the reading list. See [data layers](../data/README.md).

## Practice exercise

Draw five boxes showing how an invented player CSV and game-appearance CSV would reach a summary table. Label which files you would retain unchanged and what provenance a real input would need. Don't compute a real project result yet.

## Before moving on

- [ ] I can explain ETL/ELT without naming a cloud platform.
- [ ] I can distinguish raw, cleaned and analytical files.
- [ ] I know the grain and schema are part of the data contract.
- [ ] I can explain why a source year, acquisition time and transformation version are different.
