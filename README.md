# Tigers Double-A Data Quality and Peer Context Assessment

A beginner project starter for Henry: an engineer learning Python, SQL and reliable baseball data workflows. The assignment is **unfinished by design**. There are no completed project queries, findings or charts here.

**Your question:** How trustworthy are the Erie and Eastern League batting records, and what checks are needed before comparing hitters by age and opportunity?

Follow: raw data → validation → SQL exploration → findings → recommendations. Aim for 20 hours over 14 days; focus on one Tigers affiliate, its league peers and one completed season (2025). No machine learning or production infrastructure.

## Start here

1. Read [the assignment](PROJECT_BRIEF.md) and write your population definition in your own words.
2. With your mentor, complete the [source access/use checkpoint](resources/DATA_SOURCES.md). The mentor provides an authorized local MLB snapshot before real-data work. FanGraphs is not required. Review intended public outputs separately; access alone does not grant redistribution rights.
3. Follow [setup instructions](GETTING_STARTED.md), then work through [the two-week plan](CHECKPOINTS.md).

| Guide | Purpose |
|---|---|
| [Learning modules](learning/README.md) | Seven short engineering-oriented explanations and exercises |
| [Data sources](resources/DATA_SOURCES.md) | Selected Tigers acquisition route, limitations and optional later extension |
| [Dictionary](resources/DATA_DICTIONARY.md) | Confirmed schema versus definitions needing verification; your additions |
| [Reading list](resources/REFERENCE_MATERIALS.md) | Targeted official readings with time limits |
| [Baseball context](resources/BASEBALL_CONTEXT.md) | Levels, ages, opportunities, rates and optional international context |
| [Source work](src/README.md), [SQL work](sql/README.md) | What you implement and how to organize it |
| [Report outline](reports/FINDINGS_TEMPLATE.md) | Questions to answer, not filled-in results |

## What is provided

- An assignment, checkpoints and resource/dictionary templates.
- Two **invented teaching CSVs**, a small practice-only SQL example, and tests for a basic teaching utility. They are not real source evidence or a replacement cohort.
- A setup smoke check and raw-input download helper. The download helper performs acquisition only, not project analysis.

You must implement your own source loading, validation, SQL questions, charts and findings. Passing the provided tests only validates the teaching utility and environment—not the portfolio analysis. Mentor-only research provenance is described in [HANDOFF.md](HANDOFF.md); Henry should not read completed discovery analyses before attempting his own audit.

## Data and publishing

The public starter ZIP includes no real player records, scouting narratives or completed discovery results. A separate local input snapshot is prepared for the learning exercise; it remains outside Git. Keep all real inputs under ignored data/raw and outputs under data/processed or reports/generated. Ignore notebook files until you deliberately clear private/copyrighted outputs and review them. A .gitignore protects paths, not permission: check everything staged before publishing.

This is a local starter, not yet a published GitHub repository. The mentor should review the source route and scope before handing it over and review the finished contents before any public push. No template text is a claim that Henry completed the work.
