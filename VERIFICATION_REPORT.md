# Verification Report

Local `RUN_ALL.sh` completed and printed `AXZ_RUN_ALL_PASS`.

STDOUT tail:

```text
{
  "actual": {
    "d1": [
      2,
      1
    ],
    "d2": [
      2,
      2
    ],
    "d3": [
      1,
      2
    ]
  },
  "expected": {
    "d1": [
      2,
      1
    ],
    "d2": [
      2,
      2
    ],
    "d3": [
      1,
      2
    ]
  },
  "valid": true
}
{
  "actual": {
    "d1": [
      2,
      1
    ],
    "d2": [
      1,
      2
    ],
    "d3": [
      1,
      1
    ]
  },
  "expected": {
    "d1": [
      2,
      1
    ],
    "d2": [
      1,
      2
    ],
    "d3": [
      1,
      1
    ]
  },
  "valid": true
}
{
  "actual": {
    "d1": [
      1,
      1
    ],
    "d2": [
      2,
      1
    ],
    "d3": [
      1,
      2
    ]
  },
  "expected": {
    "d1": [
      1,
      1
    ],
    "d2": [
      2,
      1
    ],
    "d3": [
      1,
      2
    ]
  },
  "valid": true
}
TEST_FULL_CHAIN_PASS
TEST_NANOGAP_REPLAY_PASS
SHA256SUMS_WRITTEN
AXZ_RUN_ALL_PASS

```

STDERR:

```text

```

## Legacy cleanup pass verification

Clean-package verification target:

```text
RUN_ALL.sh: PASS
pytest: 7 passed
sha256sum -c SHA256SUMS.txt: PASS
cache files: removed
```
