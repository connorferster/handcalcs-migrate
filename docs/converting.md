# Convert your calculations

## One notebook or script

```console
$ handcalcs-migrate beam.ipynb
converted         beam.ipynb  (6 changes, 0 warnings)

1 file converted, 0 already fine, 0 warnings.
Wrote beam_v2.ipynb
```

The converted copy is written next to the original, with `_v2` added to its
name. Use `-o` to choose the name, and `-f` to overwrite a file that's already
there. Python files (`.py`) are converted the same way.

## A folder of calculations

```console
$ handcalcs-migrate calcs/ -o calcs-v2 --report report.md
converted         Concrete/Basic Beam Shear.ipynb  (4 changes, 0 warnings)
converted         Wood/Nails in single shear.ipynb  (14 changes, 0 warnings)
...
6 files converted, 0 already fine, 1 copied, 0 warnings.
Wrote calcs-v2
Report: report.md
```

The whole folder is copied, with every file in it, and the notebooks and
Python files in the copy are converted. Files that don't use handcalcs are
copied as they are. `--only-converted` writes only the notebooks and Python
files.

`.git`, `.ipynb_checkpoints`, `__pycache__`, `.venv` and `.DS_Store` are always skipped;
`--exclude PATTERN` skips more (it can be given more than once).

## A suggested workflow

1. See what would change, without writing anything:

   ```console
   $ handcalcs-migrate calcs/ --dry-run --report report.md
   ```

2. Read the warnings in `report.md` (see [](checks.md)).
3. Convert, then open a few converted notebooks with handcalcs v2 and run them.

`--clear-outputs` clears the old outputs of converted cells, so nothing v1
rendered is left in the converted notebooks until you run them again.
