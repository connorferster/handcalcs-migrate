# Command-line options

```text
handcalcs-migrate SOURCE [options]
```

`SOURCE` is a notebook (`.ipynb`), a Python file (`.py`) or a folder.

`-o`, `--output DEST`
: Where to write. The default is `SOURCE` with `_v2` added.

`-f`, `--force`
: Overwrite `DEST` if it exists.

`-n`, `--dry-run`
: Report what would change without writing anything.

`--report FILE`
: Also write the report to `FILE`, as Markdown.

`--keep-v1-precision`
: Use 3 decimal places where v1 used its default (v2's default is 5
  significant figures).

`--v1-names`
: Keep v1's nested subscripts and Greek names.

`--clear-outputs`
: Clear the outputs of converted cells.

`--exclude PATTERN`
: Skip matching files and folders. Can be given more than once.

`--only-converted`
: In a folder, write only the notebooks and Python files.

`-q`, `--quiet`
: Report only the files with warnings.

`-V`, `--version`
: Show the version and exit.
