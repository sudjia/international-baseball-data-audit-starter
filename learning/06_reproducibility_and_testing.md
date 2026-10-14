# 6. Reproducibility and testing

## Why it matters

A lab result needs a protocol; an analytical result needs runnable steps and versioned decisions. Readable, boring code is easier for your mentor and a future teammate to review than a clever chain of transformations.

## Simple explanation

Git records local changes in commits; GitHub hosts repositories/remotes for collaboration. status shows changed files, diff shows content, add stages selected changes and commit records them. A push uploads commits and is a separate reviewed action. .gitignore doesn't remove files already tracked or authorize sharing.

A virtual environment isolates installed packages; requirements.txt pins versions. Keep source, tests, documentation and queries in Git; keep restricted raw data and local databases out. Put inputs/outputs in defined directories. Prefer pathlib and a documented project root/path argument over a personal absolute laptop path.

Logs should say which source/file/stage succeeded or failed and how many records were processed. Never log credentials or entire scouting text. Clear errors are part of reproducibility; catching everything and returning an empty table can create a false success.

**Unit tests** check a small function with invented inputs. **Integration tests** check components together against permitted actual inputs. **Data validation tests** check expected schema, supported value rules, keys or relationships. A test that skips isn't evidence the real workflow ran. Avoid meaningless “assert True” tests or replacing missing source data with fake passing integration data.

An **idempotent transformation** produces the same output from the same input and rules; rerunning must not append the same rows twice. Re-querying a changing API isn't guaranteed to return the same input, so preserve a snapshot/hash and distinguish fresh acquisition from reproducible transformation.

## Baseball example

You alter the missing-string policy or aggregate levels differently. Record that rule/version, rerun the same input, and compare outputs. Don't quietly overwrite the only raw snapshot or depend on yesterday's notebook variables.

## Common mistakes

- Committing secrets, notebooks with restricted outputs or giant databases.
- Running tests in the wrong Python interpreter.
- Tests that only repeat implementation statements rather than catch defects.
- Claiming repeatability while the second run doubles stored rows.

## Recommended reading

[GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world), [pytest first steps](https://docs.pytest.org/en/stable/getting-started.html), and optional [pathlib](https://docs.python.org/3/library/pathlib.html).

## Practice exercise

Run the teaching tests and explain what they do **not** prove. Add a test to a small function you write using an invented bad input. Define a clean-run procedure with raw inputs unchanged, empty processed outputs, documented commands and a safe staged-content review.

## Before moving on

- [ ] I know local commit versus public push.
- [ ] I can explain dependencies, paths, logs and three test types.
- [ ] I can rerun a transformation without duplicating results.
- [ ] I can document a clean run and inspect staged files before publication.
