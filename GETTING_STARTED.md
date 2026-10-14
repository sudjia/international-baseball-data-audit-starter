# Getting started

## 1. Confirm the Tigers input snapshot with your mentor

Read [the brief](PROJECT_BRIEF.md) and [data access](resources/DATA_SOURCES.md). The selected route is Erie/Eastern League, 2025. The prepared snapshot or supplied download helper provides the inputs before day 4; until then use only the invented practice data. FanGraphs is an optional later extension, not a decision or access hurdle Henry needs to resolve. Review MLB terms and intended public outputs with the mentor.

### Obtain the prepared inputs without manual extraction

The mentor can hand over the separate Tigers input-snapshot ZIP with this starter. Extract both ZIPs into the same parent folder; both use the international-baseball-data-audit-starter root, so the snapshot lands in data/raw. It contains only original MLB JSON and provenance, not completed analysis. Keep the input snapshot out of public Git.

Alternatively, after installing dependencies, run:

```bash
.venv/bin/python examples/download_tigers_inputs.py
```

Windows:

```powershell
.\.venv\Scripts\python.exe examples\download_tigers_inputs.py
```

This supplied setup helper downloads/caches the three raw inputs and records provenance; Henry still writes the analytical loader and all checks/queries. With the prepared snapshot installed, it verifies hashes and uses local files without network requests. Fresh acquisition was tested during preparation. A live failure should be reported, not bypassed or replaced by invented data.

## 2. Create the Python environment

Python **3.12** is the tested version. Install it from python.org if necessary. A terminal runs commands; a .py file contains Python code. Run the following commands from this starter's root, not from the original discovery repository.

macOS/Linux:

```bash
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python examples/check_setup.py
.venv/bin/python -m pytest -q
```

Windows PowerShell (Python 3.12 installed):

```powershell
py -3.12 --version
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe examples\check_setup.py
.\.venv\Scripts\python.exe -m pytest -q
```

Using the environment's interpreter explicitly avoids activation-policy problems. In an editor, choose the same .venv interpreter. Do not install packages with sudo or disable certificate checks. Dependencies are pandas (tables), DuckDB (local SQL), matplotlib (plots), pytest (tests). No cloud account, database server, pybaseball or API token is needed for the default scope.

The smoke check prints versions, reads only invented CSVs and exercises in-memory DuckDB. Two tests check a teaching ratio function. Green results prove setup/basic utility behavior, not real-data readiness or finished analysis. Stop and read the error if either command fails.

## 3. Practice before real data

Read [module 1](learning/01_data_engineering_fundamentals.md), then use [module 2](learning/02_python_for_data_analysis.md) to inspect data/practice. Try [practice SQL](examples/practice_sql.py). These tiny examples are teaching material, not project solutions or data evidence.

## 4. Start your own work

- Put authorized original files under data/raw; do not edit them.
- Record source provenance in a local manifest. Create cleaned tables under data/processed and document each transformation.
- Create your scripts under src and your own queries under sql. Use a local DuckDB file under data/processed; define column names and IDs deliberately.
- Use [CHECKPOINTS.md](CHECKPOINTS.md) to decide what to learn/build next. Scripts are the default; notebooks are optional and need extra editor/kernel setup that is outside the core environment.

A raw-input download helper is supplied as setup support so acquisition is not Henry's first obstacle. Source acquisition reproduction is optional; the required learning work is his own loading, validation, SQL, analysis and communication. Provenance remains part of the assignment.

## 5. Work locally with Git

This starter uses a main branch. Use Git status/diff/add/commit to record your own progress after obtaining the reviewed starter. Check staged names and diffs before each commit. Don't push until the mentor reviews source rights, files and conclusions. Keep real data, scouting text, private notes, local databases and uncleared notebook outputs out of Git.

At project completion, document the actual run commands Henry implemented; don't treat these setup commands as the analytical pipeline.
