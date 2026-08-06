# Supplementary audit data

This directory contains supplementary, versioned audit artifacts for the targeted
structured review. The files are distributed under CC BY 4.0. Scripts are
distributed under the MIT License in the repository root.

The test--retest worksheet is generated with:

```bash
python3 scripts/create_test_retest_sample.py
```

The worksheet intentionally contains blank retest fields. Agreement statistics
must only be reported after the reviewer completes the retest independently and
the completed worksheet is preserved alongside the comparison script.
