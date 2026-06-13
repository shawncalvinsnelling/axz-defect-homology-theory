#!/usr/bin/env python3
import json, sys
from pathlib import Path
def shape(A): return (len(A), len(A[0]) if A else 0)
def validate(p):
    data=json.loads(Path(p).read_text()); missing=[k for k in ['name','dimensions','d1','d2','d3'] if k not in data]
    if missing: return {'valid':False,'missing':missing}
    d=data['dimensions']; C,R,G,H=d['C'],d['R'],d['G'],d['H']; exp={'d1':(R,C),'d2':(G,R),'d3':(H,G)}; act={'d1':shape(data['d1']),'d2':shape(data['d2']),'d3':shape(data['d3'])}
    return {'valid':exp==act,'expected':exp,'actual':act}
def main(argv=None):
    argv=argv or sys.argv[1:]
    if len(argv)!=1: print('Usage: validate_complex.py <complex.json>',file=sys.stderr); return 2
    out=validate(argv[0]); print(json.dumps(out,indent=2,sort_keys=True)); return 0 if out['valid'] else 1
if __name__=='__main__': raise SystemExit(main())
