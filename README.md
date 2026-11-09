# COMP 3110: Source Code Line Tracking

Python project scaffold for implementing the LHDiff approach described in the
project introduction slides. The algorithm is not implemented yet.

## Folder structure

```text
BIT_COMP3110_PROJECT/
|-- old_files/               # Original versions of files to compare
|-- new_files/               # Updated versions of the same files
|-- src/
|   `-- lhdiff/              # Python implementation
|       |-- __init__.py
|       |-- preprocessing.py # Normalize lines
|       |-- unchanged.py     # Detect unchanged lines using diff
|       |-- similarity.py    # Content/context similarity and Simhash helpers
|       |-- candidates.py    # Generate candidate line matches
|       |-- matching.py      # Resolve conflicting matches
|       |-- line_splits.py   # Detect one-to-many line mappings
|       `-- tracker.py       # Coordinate the line-tracking pipeline
|-- datasets/
|   |-- existing/            # Existing evaluation datasets and expected mappings
|   `-- contributed/         # New evaluation dataset and expected mappings
|-- results/                # Generated line mappings and evaluation reports
|-- tests/                  # Future unit and integration tests
`-- docs/                   # Design notes and project report
```

## File pairs

Use matching relative paths in `old_files/` and `new_files/`, for example
`old_files/example.java` and `new_files/example.java`. These folders hold input
files; the implementation itself is Python and should remain language independent.

## Planned implementation

1. Normalize lines and detect unchanged lines.
2. Generate candidates using Simhash of line content and surrounding context.
3. Resolve matches using content and context similarity.
4. Detect line splits and output old-to-new line mappings.
5. Evaluate against existing datasets and a contributed dataset covering at
   least 25 file pairs with known line mappings.

The slides also propose extending the tool to identify bug-introducing changes
from bug-fix changes. That extension can be added after the core tracker works.

Keep expected mappings alongside each evaluation dataset. Store generated
predictions and evaluation summaries in `results/`.

No third-party dependencies have been selected yet.
