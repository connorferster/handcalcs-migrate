# Install

handcalcs-migrate needs Python 3.11 or later and nothing else. It doesn't need
handcalcs itself: it reads and rewrites your files as text.

Install it as a command-line tool:

```console
$ pipx install handcalcs-migrate
```

or with uv:

```console
$ uv tool install handcalcs-migrate
```

Or run it once, without installing:

```console
$ uvx handcalcs-migrate calcs/
```

`python -m handcalcs_migrate` is the same command as `handcalcs-migrate`.

The converted notebooks need **handcalcs 2.0.0rc5 or later**:

```console
$ pip install --upgrade --pre handcalcs
```
