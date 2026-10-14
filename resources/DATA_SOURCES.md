# Data sources and source decision

## Mentor checkpoint before real data

The Tigers route is selected. Technical access worked during discovery; intended source use/sharing still needs applicable MLB terms review. The prepared local snapshot supplies Erie hitting, Eastern League hitting and Erie biographies with URLs, parameters, acquisition UTC timestamps and hashes. Use the separate input ZIP, or run the supplied examples/download_tigers_inputs.py helper after setup. Keep them in ignored data/raw. Henry does not need to debug live acquisition to begin learning.

No real source files or finished discovery results are bundled in this starter. The mentor's source-preparation instructions are in HANDOFF.md. FanGraphs is an optional future project whose terms and semantics remain separate issues, not a blocker for this assignment. Public release of any outputs is a later reviewed step.

## Selected route: Tigers Double-A / Eastern League audit

This is Henry's starting assignment: one Tigers affiliate and its league peers in 2025. The mentor prepares an authorized local snapshot; Henry learns loading, validation, SQL and communication. Signing-bonus analysis is excluded.

Validated metadata: Detroit Tigers MLB ID **116**, Erie SeaWolves ID **106**, Eastern League ID **113**, Double-A sport ID **12**. Discover affiliation from the requested season's metadata rather than treating it as permanent.

Small validated requests:

- [Double-A team metadata, 2025](https://statsapi.mlb.com/api/v1/teams?sportId=12&season=2025).
- [Erie 2025 batting](https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting&season=2025&sportIds=12&teamId=106&playerPool=ALL&limit=1000).
- [Eastern League 2025 batting](https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting&season=2025&sportIds=12&leagueId=113&playerPool=ALL&limit=1000).

The expected season-statistics array is nested under stats[0].splits; verify type/group rather than blindly assuming the first block in every response. Compare received rows with totalSplits and inspect pagination before claiming response completeness.

Available fields: player/team/league/sport IDs, season, position, reported season age, PA, AB, H, HR, BB, SO, OBP/SLG/OPS. Candidate grain differs between team-specific and league player-season aggregates. Biography enrichment supplies DOB/country, not signing facts. Mixed-team aggregates, rehab MLB players, rate-string sentinels and historical age conventions need validation. All response rows returned is not independent proof the source covers every player.

Fallback questions: Are IDs/ages/opportunities complete and plausible? Do team/league/biography joins preserve the expected grain? What workload and age definitions make peer summaries defensible? Build three QA/coverage queries and two age/opportunity/quality charts. No projection, career-development rate or signing eligibility claim. The fallback avoids FanGraphs content but is **not** assumed an open-data license; review MLB terms too.

## Optional later project: selected FanGraphs batting prospect board

Source: [FanGraphs](https://www.fangraphs.com/); [terms](https://www.fangraphs.com/about/terms-of-service).

Exact endpoint validated during discovery:

<https://www.fangraphs.com/api/prospects/board/prospects-list-combined?pos=all&lg=2,4,5,6,7,8,9,10,11,14,12,13,15,16,17,18,30,32,33&stats=bat&qual=0&type=0&team=&season=2021&seasonend=2021&draft=2022prospect&valueheader=prospect-new&quickleaderboard=2021all>

It returned JSON via an ordinary public GET in discovery. No supported public API contract, historical completeness guarantee or numerical rate limit was established. It is a website backend; an old Reddit URL is not documentation or permission. Never impersonate a browser to evade restrictions, bypass paywalls or retry repeatedly after denial.

If the mentor clears the intended use: make one small ordinary request (or obtain an authorized local snapshot), check HTTP status/content type and JSON structure, save original bytes under data/raw, record URL/UTC time/parameters/hash, then work from the cached file. Stop on denial, unexpected HTML or an empty response. Do not bulk iterate boards or seasons. A header-only CSV or zero-row payload does not validate a real-data workflow.

Expected arrays are **dataScout** and **dataStats**. Scouting refers to **2022**, batting to **2021**, despite the endpoint's performance-year parameters. Market label J2 denotes the source's international-amateur category; it is not proof every record signed July 2 or represents all international signees. This endpoint selects batters; no pitcher population is validated by this route.

Candidate grain: one listed prospect observation on this board; batting is a player-season aggregate that can span multiple levels. Verify key uniqueness and actual arrays on your own input. Use UPID within these arrays if validated. The statistics array's xMLBAMID may bridge to MLB biographies; do not confuse it with PlayerId or UPID. See [the dictionary](DATA_DICTIONARY.md).

Limitations: selected prospects, missing disclosures, no exact signing date, uncertain financial units/currency, undocumented country meaning, numeric-string ages/dates, mixed level strings and current-looking metadata within a historical board. Signing organization and board organization are different fields. Don't calculate precise signing age from a year or interpret every missing outcome as failure.

Terms reviewed in discovery restrict unauthorized reproduction/publication/further distribution; raw JSON includes copyrighted scouting narratives. Keep it local and ignored. Do not copy narratives, completed discovery results or raw records into the portfolio. Decide permitted treatment of derived outputs before public release; using aggregates is not an automatic legal permission.

## Optional small identity check: MLB Stats API

Service: <https://statsapi.mlb.com/api/v1/>. Community documentation: [MLB-StatsAPI wiki](https://github.com/toddrob99/MLB-StatsAPI/wiki). The wrapper is not MLB's official completeness/rights guarantee and is unnecessary for this project's dependencies.

Validated route: people?personIds= followed by a small comma-separated set of verified MLBAM IDs. Discovery also validated transaction and performance endpoints. Biographies supply id, birthDate and birthCountry; a debut field may be absent. Treat returned ID matches as identity evidence but review discrepancies, source time and semantic definitions.

Use a deliberately selected small sample only after permission/access review. Avoid name-only automatic matching, logging private data, or interpreting absent debut as known failure. Country of birth is not necessarily citizenship, residence or international signing eligibility. MLB data rights are separate from the wrapper's software license; review [MLB's copyright notice](https://gdx.mlb.com/components/copyright.txt) and applicable terms. This notice link was documented by the source, not independently reverified in starter construction.

## Provenance and learner independence

Mentor provenance: schema/access facts were checked against discovery commit 02ca4c7f44714c7a8189b201fe353456866216f9. Counts, completed quality profiles, scouting narratives and final query/chart answers were deliberately not copied. URLs may change; report actual new results, not expected discovery counts. The source-use checkpoint remains open even though access worked previously.
