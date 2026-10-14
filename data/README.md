# Data layers

- **practice/** is committed invented teaching data. It is not evidence about baseball players and must never enter the real findings/report as an observation.
- **raw/** (create locally) holds authorized original source files and a local provenance manifest. Preserve original bytes. It is ignored by Git.
- **processed/** (create locally) holds typed/transformed tables and the DuckDB file. It is ignored. Record the input hash and transformation rules.

For a real input, record URL, parameters, actual acquisition time in UTC, file hash, source observation years, access method, restrictions and intended population. A file's modification time isn't proof of acquisition time. Don't store credentials, copyrighted narrative excerpts or personal paths in a committed manifest.

At handoff, explain how an authorized reviewer obtains the real data. A public repository can contain code/documentation without redistributing the inputs. Your mentor reviews public summaries too; aggregation alone does not settle source use rights.
