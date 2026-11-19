# What it converts

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


The converted notebooks need handcalcs 2.0.0rc5 or later. For what changed
between the versions, see
[Coming from handcalcs v1](https://handcalcs.structuralpython.com/getting-started/migrating-from-v1.html).
