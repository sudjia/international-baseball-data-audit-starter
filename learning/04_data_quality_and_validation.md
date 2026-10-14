# 4. Data quality and validation

## Why it matters

Quality is fitness for a stated use, not a universal score. A file can be syntactically clean yet unsuitable for answering a scouting question. Think of validation as instrument checks, not a substitute for calibration against a trusted reference.

## Simple explanation

| Dimension | Question |
|---|---|
| Completeness | Is the required value present for the defined population? |
| Uniqueness | Does the proposed key identify each row at its grain? |
| Validity | Does a value meet supported type/domain/unit/date rules? |
| Consistency | Do related fields/sources agree where they should? |
| Accuracy | Does the value correspond to reality or a trusted reference? |
| Referential integrity | Does a referenced player ID exist in the other table? |
| Freshness | Is the observation recent enough for its use, with time meaning known? |
| Schema | Are required columns/types/structures still present? |

Report counts and rates with denominators: missing rows / eligible rows. An absent column differs from a present all-null column. Exact duplicates, legitimate repeat player observations and duplicated real-world events are different problems.

Missing-data mechanisms are hypotheses: MCAR (unrelated to data), MAR (related to observed variables), MNAR (related to unobserved/missing values). A public prospect file doesn't let you prove those assumptions. Examine patterns and explain what you cannot establish.

## Baseball example

Missing bonus means “not reported here,” not zero cost. Filling it with zero biases averages and rankings. A selected scouting board omits unlisted signees; complete values within its rows cannot make it a complete international signing population. Likewise a type check cannot establish birthplace or contract accuracy.

## Common mistakes

- Declaring accuracy because no values are missing.
- Assuming missingness is random or using tiny groups without counts.
- Enforcing undocumented grade/currency ranges or dropping flags without review.
- Calling no returned performance “never played.”

## Recommended reading

[pandas introductory missing-data tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) and [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html). Mentor discussion is more useful than an extra theory course here.

## Practice exercise

Write a six-row **invented** table on paper containing missing values, an impossible negative count, repeated player observations and a duplicated event. Define three checks with input, expected warning/failure and denominator. Explain which checks could not establish accuracy.

## Before moving on

- [ ] I can distinguish all dimensions above with an example.
- [ ] I can specify a metric and its eligible denominator.
- [ ] I do not equate missing with zero or coverage with census completeness.
- [ ] I preserve flagged records and record review decisions.
