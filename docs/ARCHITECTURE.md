# Architecture

```text
JSON complex → dimension validation → d2*d1 check → d3*d2 check → GF(2) rank/nullity → H_R/H_G → nano-gap → receipt replay → truth label
```

Failure modes:

| Failure | Meaning |
|---|---|
| \(\partial_2\partial_1\ne0\) | residual map is not chain-compatible |
| \(\partial_3\partial_2\ne0\) | gate-to-receipt map is not chain-compatible |
| \(H_R\ne0\) | unexplained residual defect |
| \(H_G\ne0\) | unrecepted gate obligation |
| \(\varepsilon_i\ge\Gamma_i\) | nano-gap instability |
| receipt replay mismatch | audit object not stable |
