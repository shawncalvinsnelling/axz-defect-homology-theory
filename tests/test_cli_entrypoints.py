#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=True)


def test_defect_homology_cli_closed_example():
    result = run([sys.executable, 'verifier/defect_homology.py', 'examples/full_closed_chain.json'])
    assert 'AXZ_FULL_CHAIN_CLOSED' in result.stdout


def test_nanogap_cli_closed_example():
    result = run([sys.executable, 'verifier/nano_gap_stability.py', 'examples/full_closed_chain.json'])
    assert 'NANO_GAP_STABLE' in result.stdout
