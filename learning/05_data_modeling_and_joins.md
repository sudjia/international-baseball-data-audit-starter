# 5. Data modeling and joins

## Why it matters

Joining is a measurement-design decision. If each record means something different, matching a label can quietly change your unit of analysis and inflate counts.

## Simple explanation

**Grain** means what one row represents: a player, a player-season, a player-team-season, or a pitch. Write it as a sentence. A player can have many performance rows; a stable ID identifies the person, not necessarily the observation.

One-to-one means each key appears at most once on both sides. One-to-many means one player matches several observations. Many-to-many occurs when both sides repeat the join key; it can generate a Cartesian product within each key. pandas merge(validate=...) checks an intended relationship. indicator=True helps expose unmatched rows; measure missing keys separately.

SQL normally doesn't match NULL keys. pandas can match missing keys to each other; quarantine or explicitly handle missing IDs rather than let unknown players match. An ID should keep its source namespace—FanGraphs and MLB identifiers are not interchangeable just because both look numeric.

**Entity resolution** is deciding whether records describe the same person. Start with documented IDs, then review corroborating evidence. Names can contain aliases, accents or collisions. Preserve unresolved matches; don't silently fuzzy-match them. A DOB disagreement can indicate identity, formatting or source-quality problems, not a known correction rule.

## Baseball example: invented row multiplication

Player P0 has two invented scouting updates and three game-appearance rows. Joining solely on player_id produces **six rows**, not two or three. Counting that result as six players is wrong; summing a player-level amount would repeat it. Define whether you need an update, a season, or a game before choosing the relationship or aggregation.

Player-season aggregates spanning levels cannot silently become level-specific peers. A team shown on an aggregate also may not own every underlying observation.

## Common mistakes

- Blindly deduplicating by player ID when multiple seasons are legitimate.
- Treating unmatched players as zero performance.
- Joining current teams to original signing organizations.
- Hiding row multiplication with DISTINCT instead of fixing the grain.

## Recommended reading

[pandas merging guide](https://pandas.pydata.org/docs/user_guide/merging.html) and [DuckDB joins](https://duckdb.org/docs/stable/sql/query_syntax/from.html), targeted to cardinality and null behavior.

## Practice exercise

Use invented players.csv and appearances.csv. Draw their relationship and predict the joined grain before trying it. Then invent two rows with the same player ID in a second table and predict a many-to-many join's row count. Write a key map for the real project before implementing it.

## Before moving on

- [ ] I can state the grain and key of each table.
- [ ] I can predict one-to-many and many-to-many row behavior.
- [ ] I report unmatched/missing keys, not just matches.
- [ ] I can explain why stable IDs and namespace matter more than names.
