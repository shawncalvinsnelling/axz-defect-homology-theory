# AXZ Defect Homology Theory — Ultimate Release

> Visible-upload package note: this repository package contains no hidden files. The core code, tests, receipts, docs, schemas, and paper scaffold are included. GitHub Actions can be enabled later by copying `GITHUB_ACTIONS_WORKFLOW_VERIFY_YML_VISIBLE_COPY.txt` into `.github/workflows/verify.yml`.


[![AXZ Verification](https://github.com/shawncalvinsnelling/axz-defect-homology-theory/actions/workflows/verify.yml/badge.svg)](https://github.com/shawncalvinsnelling/axz-defect-homology-theory/actions/workflows/verify.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-finite%20proof--audit-blue.svg)](CLAIM_STATUS.md)

**Primary theorem:** the Snelling Defect Homology Theorem  
**Subtitle:** a finite topological certificate theory for claims, residuals, gates, and receipts.

AXZ Defect Homology Theory is a complete finite proof-audit framework. It turns a bounded verification system into a chain-complex-style audit object over `F₂`, computes obstruction classes, checks nano-gap stability, and replays cryptographic receipts.

```text
Claim → Residual → Gate → Receipt → Truth Label
```

## Truth boundary

This repository does **not** claim to solve RH, P vs NP, Erdős–Straus globally, Navier–Stokes, Hodge, Beal, or any other infinite/global conjecture. It provides a finite verification and proof-audit framework for bounded systems.

## Core complex

```text
C --∂1--> R --∂2--> G --∂3--> H
```

where:

- `C` is claim space,
- `R` is residual / defect space,
- `G` is gate space,
- `H` is receipt space.

The required chain conditions are:

```text
∂2∂1 = 0
∂3∂2 = 0
```

The two finite AXZ obstruction groups are:

```text
H_R^AXZ(K) = ker(∂2) / im(∂1)
H_G^AXZ(K) = ker(∂3) / im(∂2)
```

A finite audit complex is closed when both groups vanish and its nano-gap receipts replay.

## Quick start

```bash
python verifier/defect_homology.py examples/full_closed_chain.json
python verifier/defect_homology.py examples/open_residual_obstruction.json
python verifier/nano_gap_stability.py examples/full_closed_chain.json
bash RUN_ALL.sh
```

Expected final line:

```text
AXZ_RUN_ALL_PASS
```

## What this ultimate release includes

- Snelling Defect Homology Theorem
- finite AXZ chain-complex verifier
- residual and gate obstruction groups
- nano-gap stability verifier
- receipt replay verifier
- JSON schemas for complexes and receipts
- closed and open obstruction examples
- bad chain-condition examples
- Erdős–Straus finite gate-complex example
- AI firewall, microscope telemetry, and SAT-to-CLIQUE finite examples
- SHA256 integrity manifest
- GitHub Actions verification workflow
- architecture, API, reproducibility, and truth-boundary docs
- formal paper scaffold
- public landing page
- professor audit checklist

## Repository map

```text
.github/workflows/verify.yml      CI replay workflow
core-laws/                         AXZ root-law context
schemas/                           JSON schemas for complexes and receipts
docs/                              architecture, truth boundary, API, reproducibility
examples/                          closed/open finite complexes and demos
receipts/                          replay receipts and release manifest
verifier/                          Python verification engines
tests/                             pytest suite
paper/                             formal paper scaffold
public/                            simple landing page
```


## GitHub Pages working landing page

This upload includes a root `index.html` plus `public/index.html`. After uploading to GitHub, enable Pages with:

```text
Settings → Pages → Deploy from a branch → main → / root
```

The live site will open at:

```text
https://shawncalvinsnelling.github.io/axz-defect-homology-theory/
```

No hidden files are required for the landing page to work.

## Claim standard

The AXZ standard is:

```text
Idea → invariant → residual → defect → gate → certificate → receipt → truth label
```

A claim without replayable evidence is not treated as closed.

## Recommended GitHub release

Use a single public release tag:

```text
ultimate
```

Release title:

```text
AXZ Defect Homology Theory — Ultimate Release
```

## Citation

Use `CITATION.cff` for citation metadata. Recommended short description:

> AXZ Defect Homology Theory is a finite proof-audit framework for computing obstruction classes, checking nano-gap stability, and replaying verification receipts in bounded claim systems.
