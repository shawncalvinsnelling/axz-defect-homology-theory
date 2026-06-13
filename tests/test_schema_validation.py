#!/usr/bin/env python3
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


def test_examples_match_axz_complex_schema():
    schema = json.loads((ROOT / 'schemas' / 'axz_complex.schema.json').read_text())
    for p in (ROOT / 'examples').glob('*.json'):
        data = json.loads(p.read_text())
        jsonschema.validate(data, schema)


def test_generated_homology_receipts_match_schema_when_present():
    schema = json.loads((ROOT / 'schemas' / 'axz_receipt.schema.json').read_text())
    for p in (ROOT / 'receipts').glob('*_homology.json'):
        data = json.loads(p.read_text())
        jsonschema.validate(data, schema)
