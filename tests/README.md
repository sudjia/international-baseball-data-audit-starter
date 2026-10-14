# Henry's tests go here

The two provided tests only check a teaching ratio. They are not evidence about real source data or a completed audit. Add your own meaningful tests for the checks you implement: missing required columns, invalid conversion/value behavior, key violations and unsafe joins.

Use invented fixtures for unit tests and label them. Real-data integration checks need authorized input and must not silently replace it with practice data. A skipped integration test must be reported as skipped, not passed. Keep private/raw fixtures outside Git.

Run from the repository root: .venv/bin/python -m pytest -q (Windows: the .venv Scripts interpreter). Explain what failure each test is designed to catch.
