# Mentor handoff: review before sharing

## Provenance, not a solution pack

This starter was informed by source schemas, routes and limitations at discovery commit **02ca4c7f44714c7a8189b201fe353456866216f9** in sudjia/baseball-data-exploration. It does not copy completed profiles, queries, quality counts, narratives, findings or charts. The original repository is unchanged. Keep its completed analyses mentor-only until Henry attempts his own audit.

## Decisions before Henry starts

1. The **Tigers 2025 Erie/Eastern League route is selected** to minimize first-project acquisition and interpretation hurdles. Review applicable MLB terms and intended public outputs; FanGraphs is not required.
2. The verified local snapshot is prepared in ignored data/raw, with original Erie hitting, Eastern League hitting, Erie biographies and provenance. A separate input ZIP can accompany the starter for private learning. No manual extraction is needed. Alternatively Henry runs examples/download_tigers_inputs.py after setup. The downloader supports acquisition only, not finished analysis; keep source data out of public Git.
3. Agree on the 20-hour scope, three mentor meetings and reviewed outputs. Keep completed discovery analyses mentor-only.
4. Review this starter before any remote creation/push. No real source data is bundled in the public code ZIP. Check Git staging and cleared notebook outputs again before publication.

The starter's supplied raw-input helper was checked on both saved files and fresh requests. It keeps URL/time/hash metadata and refuses to overwrite conflicting local inputs. The input ZIP contains no quality profiles, query answers or charts. It does not grant an open-data redistribution license; applicable MLB terms continue to apply.

## Keep accountability separate from claims

Use checkpoint evidence, not a promise of completion: runnable loading code, explained quality rules, reviewed SQL, then charts/report/presentation. A template or AI-generated assignment is not Henry's analytical experience.

## Construction checks and limitations

The core setup must install from requirements.txt, exercise in-memory DuckDB/read invented CSVs, and pass two teaching-utility tests. These do not validate Henry's real-data pipeline. See resources/LINK_CHECK.md for attempted external-link verification; proxy-blocked URLs remain unverified. Core notebooks aren't required. Windows commands are documented; only Linux/Python 3.12 execution is validated here.

Data rights and Henry's actual source pipeline are intentionally unresolved until the first mentor checkpoint. GitHub upload is handled separately from local preparation; check the actual remote/commit status before sharing a repository link.
