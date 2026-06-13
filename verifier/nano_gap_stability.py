#!/usr/bin/env python3
import json, hashlib, sys
from pathlib import Path

def verify(data):
    results=[]; ok=True
    for g in data.get('nano_gap_gates',[]):
        gamma=float(g['gamma']); eps=float(g['epsilon']); stable=eps<gamma; ok=ok and stable
        results.append({'gate_id':g.get('gate_id'),'gamma':gamma,'epsilon':eps,'margin':gamma-eps,'stable':stable})
    out={'name':data.get('name'),'gates_checked':len(results),'all_stable':ok,'results':results,'truth_label':'NANO_GAP_STABLE' if ok else 'NANO_GAP_UNSTABLE'}
    out['receipt_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True).encode()).hexdigest(); return out

def main(argv=None):
    argv=argv or sys.argv[1:]
    if len(argv)!=1: print('Usage: nano_gap_stability.py <complex.json>',file=sys.stderr); return 2
    out=verify(json.loads(Path(argv[0]).read_text())); print(json.dumps(out,indent=2,sort_keys=True)); return 0 if out['all_stable'] else 1
if __name__=='__main__': raise SystemExit(main())
