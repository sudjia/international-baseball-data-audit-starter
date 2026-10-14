# External link checks

Official reference URLs were tested with ordinary HTTPS requests during starter construction. Reachable means the request returned a successful HTTP status. Proxy-blocked means this environment could not reach the domain; the URL remains unverified, not proven broken. No protections or TLS checks were bypassed.

| Resource | Outcome | URL |
|---|---|---|
| python_tutorial | Unverified: proxy CONNECT 403 | <https://docs.python.org/3/tutorial/introduction.html> |
| python_json | Unverified: proxy CONNECT 403 | <https://docs.python.org/3/library/json.html> |
| python_errors | Unverified: proxy CONNECT 403 | <https://docs.python.org/3/tutorial/errors.html> |
| pandas_intro | Unverified: proxy CONNECT 403 | <https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html> |
| pandas_merge | Unverified: proxy CONNECT 403 | <https://pandas.pydata.org/docs/user_guide/merging.html> |
| duckdb_python | Unverified: proxy CONNECT 403 | <https://duckdb.org/docs/stable/clients/python/overview.html> |
| duckdb_select | Unverified: proxy CONNECT 403 | <https://duckdb.org/docs/stable/sql/query_syntax/select.html> |
| duckdb_join | Unverified: proxy CONNECT 403 | <https://duckdb.org/docs/stable/sql/query_syntax/from.html> |
| duckdb_null | Unverified: proxy CONNECT 403 | <https://duckdb.org/docs/stable/sql/data_types/nulls.html> |
| github_intro | Unverified: proxy CONNECT 403 | <https://docs.github.com/en/get-started/start-your-journey/hello-world> |
| pytest | Unverified: proxy CONNECT 403 | <https://docs.pytest.org/en/stable/getting-started.html> |
| matplotlib | Unverified: proxy CONNECT 403 | <https://matplotlib.org/stable/tutorials/pyplot.html> |
| fangraphs_library | Unverified: proxy CONNECT 403 | <https://library.fangraphs.com/> |
| fangraphs_terms | HTTP 200 | <https://www.fangraphs.com/about/terms-of-service> |
| mlb_glossary | HTTP 200 | <https://www.mlb.com/glossary/standard-stats> |
| python_pathlib | Unverified: proxy CONNECT 403 | <https://docs.python.org/3/library/pathlib.html> |

Source API access/schema observations in DATA_SOURCES.md come from the earlier discovery stage. No new real FanGraphs inputs were downloaded or copied into this starter. Recheck the intended source and use rights at the first mentor meeting; previous technical access is not a current API or redistribution guarantee.

The internal lessons remain usable when documentation links are blocked. A mentor can verify/open those official resources in their ordinary browser; no proxy configuration change is required to use the starter teaching examples.
