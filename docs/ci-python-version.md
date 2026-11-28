# CI Fix: Update Python version

The current CI workflow requests Python 3.9, which is no longer available on Ubuntu 26.04 runners.

**Change in `.github/workflows/` (example):**

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: "3.11"   # was 3.9
```

This resolves the "Version 3.9 was not found in the local cache" error.
