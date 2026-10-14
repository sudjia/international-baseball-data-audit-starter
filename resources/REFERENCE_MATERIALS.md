# Targeted reading, not a course catalog

Required external reading totals **135 minutes**. Internal modules total roughly 70 minutes, for about **3 hours 25 minutes** overall. These minutes are included in CHECKPOINTS, not added to it. Stop at the named topics; do not read full manuals.

Link checks were attempted in this environment. FanGraphs terms and MLB glossary were reachable; other official documentation requests were proxy-blocked. A block does not prove a URL is broken. See [link-check evidence](LINK_CHECK.md); do not describe blocked links as verified. Use the internal module and mentor/browser access if necessary.

## Required reading

| Resource / what to read | Why / stage | Minutes |
|---|---|---:|
| [Python introduction](https://docs.python.org/3/tutorial/introduction.html): values, lists, strings; skim basic functions via tutorial navigation | Translate MATLAB/Excel habits; days 2–3 | 20 |
| [JSON](https://docs.python.org/3/library/json.html): loads/load; [exceptions](https://docs.python.org/3/tutorial/errors.html): try/except | Read structure and explain failures; days 3–4 | 10 |
| [pandas intro](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html): table reading, subset selection, summary statistics, combining tables | Learn the operations actually needed; days 3–6 | 25 |
| [DuckDB Python](https://duckdb.org/docs/stable/clients/python/overview.html) and [SELECT](https://duckdb.org/docs/stable/sql/query_syntax/select.html): connect, execute, select/filter/group | Run readable local SQL; day 8 | 25 |
| [DuckDB FROM/joins](https://duckdb.org/docs/stable/sql/query_syntax/from.html) and [NULL](https://duckdb.org/docs/stable/sql/data_types/nulls.html): left/inner behavior and null comparisons | Correct joins/denominators; days 8–9 | 15 |
| [GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world): repository, branch, commit; publishing is a later reviewed step | Version your work, not restricted data; days 2/13 | 10 |
| [pytest](https://docs.pytest.org/en/stable/getting-started.html): first test and exception assertions | Test useful failure cases; days 6/13 | 10 |
| [Matplotlib pyplot](https://matplotlib.org/stable/tutorials/pyplot.html): one plot, labels, axes | Communicate two questions clearly; day 11 | 10 |
| Applicable MLB source terms with the mentor; [copyright notice](https://gdx.mlb.com/components/copyright.txt) is an entry point, not a complete permission grant | Source/use checkpoint; day 1; uncertainty doesn't authorize sharing | 10 |

All rows in this table are required topics; the selected Tigers route uses MLB terms discussion, not FanGraphs as an added assignment. The mentor owns unresolved permissions decisions; Henry should understand the restriction without spending the project doing legal research.

## Optional, only when needed

| Resource / targeted topic | Why / stage | Minutes |
|---|---|---:|
| [pandas merge guide](https://pandas.pydata.org/docs/user_guide/merging.html): validation, indicator, null warning | Join debugging, day 9 | 10 |
| [pathlib](https://docs.python.org/3/library/pathlib.html): Path, read/write, parent | Portable script paths, days 4/13 | 10 |
| [FanGraphs Library](https://library.fangraphs.com/): a metric actually used, e.g. OBP or wRC+ | Separate definition from cross-level interpretation, day 11 | 10 |
| [MLB standard-stat glossary](https://www.mlb.com/glossary/standard-stats): PA, OBP, SLG | Baseball vocabulary, fallback / day 11 | 5 |

No books, multi-hour courses or advanced engineering platforms are necessary. Before using a definition in the report, cite the relevant page and state whether it applies to the source's aggregation. A generic MLB definition doesn't prove how a prospect backend computed a multi-level statistic.
