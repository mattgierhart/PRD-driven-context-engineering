# Kuzu upstream pin

This evaluation uses the exact upstream repository supplied for the experiment:

- Repository: <https://github.com/kuzudb/kuzu>
- Release: `v0.11.3`
- Commit: `27cba5b91423c96a0a0507c92dfe0e1654f7f184`
- License: MIT
- Repository status: archived read-only by its owner on 2025-10-10

`bootstrap.sh` makes a shallow local clone at `.runtime/kuzu-source`, verifies
the checked-out commit, and installs the hash-pinned CPython 3.11 macOS ARM64
wheel into the isolated `.venv`.

The source checkout and virtual environment are local proof artifacts. They are
ignored by git because vendoring an archived C++ repository and a platform-specific
wheel would make this methodology repository larger without improving reproducibility.
