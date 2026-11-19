# What to check

Some v1 code has no direct v2 equivalent. It is converted as far as it can be,
and listed under **warnings**, in the terminal and in the `--report` file:

- `@handcalc(left=..., right=...)` and `@handcalc(record=True)`.
- Uses of a decorated function's result other than `latex, value = f(...)`:
  v1 returned `(latex, value)` and v2 returns `(value, latex)`.
- `custom_symbols`, `custom_brackets`, `greek_exclusions` and other removed
  options.

`-q` / `--quiet` lists only the files with warnings.

## Things that look a little different

These aren't warnings, but you may notice them in the rendered output:

- **Names.** `x_a_b` is x<sub>a,b</sub> in v2 (not nested subscripts), and
  `phiM` is φM. `--v1-names` keeps the v1 look.
- **Precision.** v2's default is 5 significant figures, where v1's was 3
  decimal places. `--keep-v1-precision` writes `.3f` where v1 used its default.
