#!/usr/bin/env python3
import json, hashlib, sys
from pathlib import Path
KEYS=['receipt_sha256','outer_sha256','manifest_sha256']
def replay(p):
    data=json.loads(Path(p).read_text()); key=next((k for k in KEYS if k in data),None)
    if not key: return {'file':str(p),'replay_ok':False,'reason':'no supported hash key'}
    stored=data[key]; payload=dict(data); payload.pop(key,None)
    recomputed=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
    return {'file':str(p),'hash_key':key,'stored':stored,'recomputed':recomputed,'replay_ok':stored==recomputed,'truth_label':'RECEIPT_REPLAY_PASS' if stored==recomputed else 'RECEIPT_REPLAY_FAIL'}
def main(argv=None):
    argv=argv or sys.argv[1:]
    if not argv: print('Usage: receipt_replay.py <receipt.json> [...]',file=sys.stderr); return 2
    results=[replay(p) for p in argv]; out={'checked':len(results),'all_replay_ok':all(r['replay_ok'] for r in results),'results':results}
    out['receipt_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True).encode()).hexdigest(); print(json.dumps(out,indent=2,sort_keys=True)); return 0 if out['all_replay_ok'] else 1
if __name__=='__main__': raise SystemExit(main())
