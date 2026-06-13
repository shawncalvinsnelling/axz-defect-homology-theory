#!/usr/bin/env bash
set -euo pipefail
mkdir -p receipts

python verifier/validate_complex.py examples/full_closed_chain.json
python verifier/validate_complex.py examples/open_residual_obstruction.json
python verifier/validate_complex.py examples/open_gate_receipt_obstruction.json

python verifier/defect_homology.py examples/full_closed_chain.json > receipts/full_closed_chain_homology.json
python verifier/defect_homology.py examples/open_residual_obstruction.json > receipts/open_residual_obstruction_homology.json
python verifier/defect_homology.py examples/open_gate_receipt_obstruction.json > receipts/open_gate_receipt_obstruction_homology.json
python verifier/defect_homology.py examples/erdos_straus_gate_complex.json > receipts/erdos_straus_gate_complex_homology.json
python verifier/defect_homology.py examples/ai_firewall_complex.json > receipts/ai_firewall_complex_homology.json
python verifier/defect_homology.py examples/microscope_telemetry_complex.json > receipts/microscope_telemetry_complex_homology.json
python verifier/defect_homology.py examples/sat_clique_reduction_complex.json > receipts/sat_clique_reduction_complex_homology.json

if python verifier/defect_homology.py examples/bad_chain_d2d1.json > receipts/bad_chain_d2d1_homology.json; then
  echo 'Expected bad_chain_d2d1.json to fail chain condition' >&2
  exit 1
fi
if python verifier/defect_homology.py examples/bad_chain_d3d2.json > receipts/bad_chain_d3d2_homology.json; then
  echo 'Expected bad_chain_d3d2.json to fail chain condition' >&2
  exit 1
fi

python verifier/nano_gap_stability.py examples/full_closed_chain.json > receipts/full_closed_chain_nanogap.json
python verifier/nano_gap_stability.py examples/microscope_telemetry_complex.json > receipts/microscope_telemetry_nanogap.json
python verifier/receipt_replay.py receipts/*_homology.json receipts/*_nanogap.json > receipts/receipt_replay_report.json
python tests/test_full_chain.py
python tests/test_nanogap_and_replay.py
python scripts/generate_sha256.py
echo AXZ_RUN_ALL_PASS
