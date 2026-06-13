# Formal Specification

## Input object

An AXZ complex is a finite object over \(\mathbb F_2\):

```json
{
  "name": "example",
  "dimensions": {"C": 1, "R": 2, "G": 1, "H": 0},
  "d1": [[1], [0]],
  "d2": [[0, 1]],
  "d3": [],
  "nano_gap_gates": [{"gate_id": "G0", "gamma": 0.1, "epsilon": 0.01}]
}
```

The expected shapes are:

```text
d1: R × C
d2: G × R
d3: H × G
```

## Output object

The verifier outputs ranks, nullities, homology dimensions, closure labels, and a deterministic `receipt_sha256`.

## Closure criterion

```text
full_axz_closed = chain_condition && dim_HR_AXZ == 0 && dim_HG_AXZ == 0
```
