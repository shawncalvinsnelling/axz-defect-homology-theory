#!/usr/bin/env python3
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verifier.nano_gap_stability import verify


def test_full_closed_chain_nanogap_stable():
    o = verify(json.loads((ROOT / 'examples/full_closed_chain.json').read_text()))
    assert o['all_stable']


def test_receipt_replay_script_exists():
    assert (ROOT / 'verifier' / 'receipt_replay.py').exists()


def main():
    test_full_closed_chain_nanogap_stable()
    test_receipt_replay_script_exists()
    print('TEST_NANOGAP_REPLAY_PASS')


if __name__ == '__main__':
    main()
