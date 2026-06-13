# API Reference

## defect_homology.py

```bash
python verifier/defect_homology.py examples/full_closed_chain.json
```

Returns a JSON receipt with:

- `rank_d1`, `rank_d2`, `rank_d3`
- `dim_HR_AXZ`, `dim_HG_AXZ`
- `full_axz_closed`
- `truth_label`
- `receipt_sha256`

## nano_gap_stability.py

```bash
python verifier/nano_gap_stability.py examples/full_closed_chain.json
```

Returns whether all gates satisfy `epsilon < gamma`.

## receipt_replay.py

```bash
python verifier/receipt_replay.py receipts/*_homology.json receipts/*_nanogap.json
```

Recomputes supported receipt hashes and checks replay stability.

## validate_complex.py

```bash
python verifier/validate_complex.py examples/full_closed_chain.json
```

Checks required fields and matrix dimensions.
