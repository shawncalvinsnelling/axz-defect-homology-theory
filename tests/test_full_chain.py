#!/usr/bin/env python3
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verifier.defect_homology import verify_complex


def load(ex: str):
    return verify_complex(json.loads((ROOT / 'examples' / ex).read_text()))


def test_full_closed_chain():
    o = load('full_closed_chain.json')
    assert o['full_axz_closed']
    assert o['dim_HR_AXZ'] == 0
    assert o['dim_HG_AXZ'] == 0


def test_open_residual_obstruction():
    o = load('open_residual_obstruction.json')
    assert o['dim_HR_AXZ'] == 1
    assert o['dim_HG_AXZ'] == 0
    assert not o['full_axz_closed']


def test_open_gate_receipt_obstruction():
    o = load('open_gate_receipt_obstruction.json')
    assert o['dim_HR_AXZ'] == 0
    assert o['dim_HG_AXZ'] == 2
    assert not o['full_axz_closed']


def test_bad_chain_d2d1_rejected():
    o = load('bad_chain_d2d1.json')
    assert not o['chain_condition_d2_d1_zero']


def test_bad_chain_d3d2_rejected():
    o = load('bad_chain_d3d2.json')
    assert not o['chain_condition_d3_d2_zero']


def main():
    test_full_closed_chain()
    test_open_residual_obstruction()
    test_open_gate_receipt_obstruction()
    test_bad_chain_d2d1_rejected()
    test_bad_chain_d3d2_rejected()
    print('TEST_FULL_CHAIN_PASS')


if __name__ == '__main__':
    main()
