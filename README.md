# handcalcs-migrate

> **This tool has moved to [StructuralPython/hc-migrate](https://github.com/StructuralPython/hc-migrate)**,
> which also turns notebooks into handcalcs v2 scripts. Use `hc-migrate ... --to ipynb`
> for what `handcalcs-migrate` did. This repository is no longer updated.

Convert Jupyter notebooks and Python files written for
[handcalcs](https://github.com/connorferster/handcalcs) v1 to handcalcs v2.

```console
$ handcalcs-migrate beam.ipynb
converted         beam.ipynb  (6 changes, 0 warnings)

1 file converted, 0 already fine, 0 warnings.
Wrote beam_v2.ipynb
```

Point it at a folder and it converts a copy of the whole tree, so a library of
calculations moves to v2 in one step:

```console
$ handcalcs-migrate calcs/ -o calcs-v2 --report report.md
converted         Concrete/Basic Beam Shear.ipynb  (4 changes, 0 warnings)
converted         Wood/Nails in single shear.ipynb  (14 changes, 0 warnings)
...
6 files converted, 0 already fine, 1 copied, 0 warnings.
Wrote calcs-v2
Report: report.md
```

**Your files are never changed.** A file is written next to the original with
`_v2` added to its name; a folder is copied to `<folder>_v2` (or `-o DEST`),
with every file in it, and the notebooks and Python files in the copy are
converted. Files that don't use handcalcs are copied as they are.

## Install

handcalcs-migrate needs Python 3.11 or later and nothing else.

```console
$ pipx install handcalcs-migrate        # or: uv tool install handcalcs-migrate
$ uvx handcalcs-migrate calcs/          # or run it once, without installing
```

The converted notebooks need handcalcs 2.0.0rc5 or later.

## What it converts

| handcalcs v1 | handcalcs v2 |
|---|---|
| `import handcalcs.render`, `%load_ext handcalcs.render` | `import handcalcs` |
| `from handcalcs.decorator import handcalc` | `from handcalcs import handcalc` |
| `%%render 2` | `%%render` with `# hc: -f .2f` |
| `%%render sci_not`, `%%render 3 sci_not` | `# hc: -f .3e` |
| `%%render long` | `# hc: -m` |
| `%%render params` | `# hc: -g` above each run of assignments (a parameter grid) |
| `%%render symbolic` | `# hc: mode = "ass sym"` |
| `%%render short` | `%%render` (the default) |
| `%%tex` (printed the LaTeX source) | `%%source latex` (prints it in v2) |
| `%%render sympy` | `# hc: -y`: a `name = name` line whose right-hand name holds a SymPy expression runs as that expression |
| `## text` between equations | `# text` (in v2, `##` is a heading) |
| a `# comment` line (v1 didn't show it) | the same comment, wrapped in `# hc: -i` / `# hc: -s` so it stays hidden |
| `x = 1  # ignore` | `x = 1  # hc: -i` |
| `@handcalc(override="long", precision=2)` | `@handcalc(LatexRenderer(), render_context={"format_code": ".2f", "multiline": True})` |
| `@handcalc(jupyter_display=True)` | `@handcalc(LatexRenderer(), display=True)` |
| a decorated function with a docstring | adds `docstring=False` (v1 didn't render docstrings) |
| `latex, value = f(...)` for a v1-decorated `f` | `value, latex = f(...)` (v2 returns the value first) |
| `set_option("display_precision", 2)` | `set_option("format_code", ".2f")` |
| `set_option("param_columns", 4)` | `set_option("param_cols", 4)` |
| options v2 removed (`latex_block_start`, `custom_symbols`, ...) | commented out, with the reason |

v1's `%%render` arguments are read exactly as v1 read them, including its
habit of accepting part of a word (`%%render param` is `params`).

## What it asks you to check

Some v1 code has no direct v2 equivalent. It is converted as far as it can be,
and listed under **warnings** (in the terminal and in `--report`):

- `@handcalc(left=..., right=...)` and `@handcalc(record=True)`.
- Uses of a decorated function's result other than `latex, value = f(...)`:
  v1 returned `(latex, value)` and v2 returns `(value, latex)`.
- `custom_symbols`, `custom_brackets`, `greek_exclusions` and other removed
  options.

Names also render a little differently in v2: `x_a_b` is x<sub>a,b</sub> (not
nested), and `phiM` is φM. `--v1-names` keeps the v1 look.

## Options

```text
-o, --output DEST     where to write (default: SOURCE with "_v2" added)
-f, --force           overwrite DEST if it exists
-n, --dry-run         report what would change without writing anything
--report FILE         also write the report to FILE (Markdown)
--keep-v1-precision   3 decimal places where v1 used its default
                      (v2's default is 5 significant figures)
--v1-names            keep v1's nested subscripts and Greek names
--clear-outputs       clear the outputs of converted cells
--exclude PATTERN     skip matching files and folders (repeatable)
--only-converted      in a folder, write only notebooks and Python files
-q, --quiet           report only files with warnings
```

`.git`, `.ipynb_checkpoints`, `__pycache__` and `.venv` are always skipped.
`python -m handcalcs_migrate` is the same command.

See the handcalcs guide,
[Coming from handcalcs v1](https://handcalcs.structuralpython.com/getting-started/migrating-from-v1.html),
for everything that changed.

## Development

```console
$ uv run --group test pytest
```

The tests convert a v1 notebook and run the result with handcalcs v2 in an
IPython shell, so every converted cell is checked to work.

## License

Apache 2.0.
