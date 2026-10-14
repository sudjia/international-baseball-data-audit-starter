# 3. SQL fundamentals

## Why it matters

SQL expresses table relationships and aggregations directly. It makes a query reviewable independently of Python's plotting code. Python can do similar work, but saved SQL helps another analyst inspect your population and denominator.

## Simple explanation

A table has rows and columns. A **primary key** uniquely identifies a row and cannot be missing; a **foreign key** references another table's key. Real source files can violate the key you hoped to use. Constraints are intentions you must validate, not proof of accurate identities.

SELECT chooses columns, WHERE filters rows before aggregation, GROUP BY creates groups, ORDER BY sorts results. COUNT(*) counts rows; COUNT(column) excludes NULL; COUNT(DISTINCT column) counts different nonnull values. NULL is unknown/missing, not zero or an empty string. Use IS NULL, not '= NULL'. Many aggregates ignore NULL, so show the denominator explicitly.

An INNER JOIN retains matches; a LEFT JOIN preserves left-side rows but can multiply them when the right key repeats. A CTE (WITH name AS (...)) names an intermediate query for readability; it does not make a join safe automatically.

DuckDB runs inside Python or as a local file. It can read CSV and work with DataFrames without a server. Declare identifiers/types deliberately rather than relying blindly on CSV inference.

```sql
-- Invented teaching table only; not a project answer.
SELECT practice_role, COUNT(*) AS people
FROM practice_players
WHERE practice_age >= 22
GROUP BY practice_role
ORDER BY people DESC;
```

See [practice_sql.py](../examples/practice_sql.py) for an unrelated in-memory teaching example. Your three project queries must answer questions you choose; don't count this practice query as a deliverable.

## Baseball example

A player-season table can have many rows per player. COUNT(*) there is not the number of players, and counting after a one-to-many join can inflate your apparent population.

## Common mistakes

- COUNT(bonus) labelled as all prospects.
- Integer arithmetic or undocumented denominators in percentages.
- Putting a right-table filter in WHERE after a LEFT JOIN and losing unmatched rows.
- Treating a display team as the full historical organization.

## Recommended reading

[DuckDB SELECT](https://duckdb.org/docs/stable/sql/query_syntax/select.html), [FROM/joins](https://duckdb.org/docs/stable/sql/query_syntax/from.html), [NULLs](https://duckdb.org/docs/stable/sql/data_types/nulls.html). Use targeted examples, not the full manual.

## Practice exercise

Use invented players/appearances to ask your own question about practice roles or games. Explain the difference between row counts and distinct players in each table. Rewrite a two-step query using a CTE; explain its NULL behavior.

## Before moving on

- [ ] I know which count includes missing values.
- [ ] I can identify primary/foreign keys and state table grain.
- [ ] I can explain INNER/LEFT behavior and a CTE.
- [ ] I can run SQL in DuckDB and describe its population in words.
