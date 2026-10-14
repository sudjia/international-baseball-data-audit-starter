# Implement your pipeline here

No real-data pipeline is supplied. Henry should write small functions/scripts whose responsibilities are clear. Suggested progression:

1. Load an authorized local input; validate the response structure and required columns; give useful errors.
2. Convert only fields whose meaning/type is established, preserving originals and reporting conversion problems.
3. Check quality/key rules and return small audit tables/issues with explicit denominators.
4. Load defined analytical tables into a local DuckDB file; state grain and source years.
5. Export permitted aggregate results for your own two charts and report.

Choose sensible filenames such as load_data.py and validate_data.py. These are suggestions, not prewritten implementations. Keep configuration/paths separate from analytical logic, and use paths relative to a defined root or passed as arguments. Never import the original discovery scripts as your completed assignment.

Document the commands you actually create in the root README. Make the pipeline fail usefully when a required input is absent rather than generate fake results. Preserve raw bytes and investigation flags.
