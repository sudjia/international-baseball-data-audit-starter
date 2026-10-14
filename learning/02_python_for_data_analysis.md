# 2. Python for data analysis

## Why it matters

Python can turn repeated Excel steps into a readable, reviewable procedure. Your MATLAB experience helps with variables/functions, but a pandas table has labelled columns and index behavior rather than just numeric arrays.

## Simple explanation

A DataFrame is a table. CSV has rows/columns; JSON can contain nested objects and arrays, so first inspect its top-level structure. Types matter: a player ID is an identifier, not a quantity. Preserve its spelling as a string. Dates, numeric measures and missing values need explicit treatment.

```python
import json
from pathlib import Path
import pandas as pd

# Invented teaching data only; run from starter root.
players = pd.read_csv("data/practice/players.csv", dtype={"player_id": "string"})
print(players.columns.tolist())
print(players.dtypes)
print(players.head())
older = players.loc[players["practice_age"] >= 22]
counts = players.groupby("practice_role").size()
# JSON structure illustration, not an API response:
payload = json.loads('{"practice_players": [{"player_id": "P0"}]}')
table = pd.json_normalize(payload["practice_players"])
```

Filtering selects rows; grouping partitions them for aggregation. isna checks recognized missing values; empty/whitespace strings may need a separate documented policy. to_numeric with errors='coerce' creates missing values from invalid input: count/report those conversions rather than hiding them. merge combines tables; validate its cardinality and inspect unmatched rows (module 5).

Write a function with an input, return value and small job. Catch the specific exception you can explain—FileNotFoundError for a missing file, ValueError for an invalid value—not every exception followed by “success.” If a request fails, preserve its status and stop that step.

## Baseball example

Missing reported bonus differs from a known zero. A column of numeric-looking strings is not automatically ready for financial interpretation, especially when units are undocumented.

## Common mistakes

- Guessing JSON structure; loading HTML as if it were JSON.
- Replacing every missing value with zero.
- Treating an ID as float, losing leading zeros or creating '.0' strings.
- Using current age for historical performance; swallowing all exceptions.

## Recommended reading

[Python introduction](https://docs.python.org/3/tutorial/introduction.html), [JSON](https://docs.python.org/3/library/json.html), [exceptions](https://docs.python.org/3/tutorial/errors.html), and [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html). Use the reading list's limits.

## Practice exercise

On invented players.csv, inspect types, choose a role filter, and count rows by role. Write a function that takes a practice-file path and returns its column names. Give a helpful error for an absent file. Do not implement the real bonus audit from this example.

## Before moving on

- [ ] I can inspect CSV and nested JSON before transforming.
- [ ] I can filter/group without modifying raw input.
- [ ] I can distinguish missing, invalid and zero.
- [ ] I can explain a reusable function and a specific exception.
