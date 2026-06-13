# Reproducibility Guide

## Local replay

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest jsonschema
bash RUN_ALL.sh
pytest -q
sha256sum -c SHA256SUMS.txt
```

## GitHub replay

The repository includes `.github/workflows/verify.yml`. After upload, the Actions tab should show `AXZ Verification` passing.

## Receipt replay

Generated receipts are deterministic JSON outputs. Replay is checked by recomputing the canonical SHA-256 digest.
