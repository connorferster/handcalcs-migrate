# handcalcs-migrate

Convert Jupyter notebooks and Python files written for
[handcalcs](https://handcalcs.structuralpython.com/) v1 to handcalcs v2.

```console
$ handcalcs-migrate beam.ipynb
converted         beam.ipynb  (6 changes, 0 warnings)

1 file converted, 0 already fine, 0 warnings.
Wrote beam_v2.ipynb
```

Point it at a folder and it converts a copy of the whole tree, so a library of
calculations moves to v2 in one step.

**Your files are never changed.** A file is written next to the original with
`_v2` added to its name; a folder is copied to `<folder>_v2` (or `-o DEST`).

```{toctree}
:maxdepth: 2

install
converting
conversions
checks
options
changelog
```

For everything that changed between v1 and v2, see the handcalcs guide,
[Coming from handcalcs v1](https://handcalcs.structuralpython.com/getting-started/migrating-from-v1.html).
