#!/usr/bin/env python3
import json, hashlib, sys
from pathlib import Path

def shape(A): return (len(A), len(A[0]) if A else 0)
def rank2(A):
    A=[row[:] for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0; c=0
    while r<m and c<n:
        piv=next((i for i in range(r,m) if A[i][c]&1),None)
        if piv is None: c+=1; continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(m):
            if i!=r and (A[i][c]&1): A[i]=[x^y for x,y in zip(A[i],A[r])]
        r+=1; c+=1
    return r

def mul2(A,B):
    if not A or not B: return []
    if len(A[0])!=len(B): raise ValueError(f'matrix mismatch: {shape(A)} x {shape(B)}')
    return [[sum(((A[i][k]&1)&(B[k][j]&1)) for k in range(len(B)))%2 for j in range(len(B[0]))] for i in range(len(A))]
def zero(A): return all((x&1)==0 for row in A for x in row)

def verify_complex(data):
    dims=data['dimensions']; C,R,G,H=dims['C'],dims['R'],dims['G'],dims['H']
    d1,d2,d3=data['d1'],data['d2'],data['d3']
    expected={'d1':(R,C),'d2':(G,R),'d3':(H,G)}; actual={'d1':shape(d1),'d2':shape(d2),'d3':shape(d3)}
    if expected!=actual:
        out={'name':data.get('name'),'dimension_check':False,'expected_shapes':expected,'actual_shapes':actual,'truth_label':'AXZ_DIMENSION_ERROR'}
    else:
        c21=zero(mul2(d2,d1)); c32=zero(mul2(d3,d2))
        rd1,rd2,rd3=rank2(d1),rank2(d2),rank2(d3)
        null_d2=R-rd2; null_d3=G-rd3
        dim_HR=null_d2-rd1 if c21 else None; dim_HG=null_d3-rd2 if c32 else None
        full_chain=c21 and c32; full_closed=full_chain and dim_HR==0 and dim_HG==0
        label='AXZ_CHAIN_CONDITION_FAIL' if not full_chain else ('AXZ_FULL_CHAIN_CLOSED' if full_closed else 'AXZ_OPEN_CHAIN_OBSTRUCTION')
        out={'name':data.get('name'),'dimension_check':True,'chain_condition_d2_d1_zero':c21,'chain_condition_d3_d2_zero':c32,'full_chain_complex':full_chain,'rank_d1':rd1,'rank_d2':rd2,'rank_d3':rd3,'nullity_d2':null_d2,'nullity_d3':null_d3,'dim_HR_AXZ':dim_HR,'dim_HG_AXZ':dim_HG,'residual_defect_closed':dim_HR==0,'gate_receipt_closed':dim_HG==0,'full_axz_closed':full_closed,'truth_label':label}
    out['receipt_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True).encode()).hexdigest()
    return out

def main(argv=None):
    argv=argv or sys.argv[1:]
    if len(argv)!=1:
        print('Usage: defect_homology.py <complex.json>',file=sys.stderr); return 2
    out=verify_complex(json.loads(Path(argv[0]).read_text()))
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out.get('dimension_check') and out.get('full_chain_complex') else 1
if __name__=='__main__': raise SystemExit(main())
