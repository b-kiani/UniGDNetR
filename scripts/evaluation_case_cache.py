"""Atomic case metrics and exact post-case RNG state for resumable evaluation."""
import base64
import hashlib
import json
import math
import os
from pathlib import Path
import numpy as np


def _safe(value):
    if isinstance(value,float) and not math.isfinite(value):
        return {'__float__':'nan' if math.isnan(value) else ('inf' if value>0 else '-inf')}
    if isinstance(value,dict):return {key:_safe(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)):return [_safe(item) for item in value]
    return value


def _unsafe(value):
    if isinstance(value,dict):
        if set(value)=={'__float__'}:return float(value['__float__'])
        return {key:_unsafe(item) for key,item in value.items()}
    if isinstance(value,list):return [_unsafe(item) for item in value]
    return value


def _canonical(value):
    return json.dumps(_safe(value),sort_keys=True,separators=(',',':'),allow_nan=False).encode()


def _bytes(state):
    array=state.cpu().numpy() if hasattr(state,'cpu') else np.asarray(state)
    return base64.b64encode(np.asarray(array,dtype=np.uint8).tobytes()).decode('ascii')


def pack_rng(state):
    name,keys,pos,has_gauss,cached=state['numpy']
    return {'python':state['python'],'numpy':[name,keys.tolist(),int(pos),int(has_gauss),float(cached)],
            'torch':_bytes(state['torch']),
            'cuda':None if state.get('cuda') is None else [_bytes(item) for item in state['cuda']]}


def unpack_rng(state,tensor_from_bytes):
    def tuples(value):return tuple(tuples(item) for item in value) if isinstance(value,(tuple,list)) else value
    name,keys,pos,has_gauss,cached=state['numpy']
    return {'python':tuples(state['python']),
            'numpy':(name,np.array(keys,dtype=np.uint32),int(pos),int(has_gauss),float(cached)),
            'torch':tensor_from_bytes(base64.b64decode(state['torch'],validate=True)),
            'cuda':None if state['cuda'] is None else [tensor_from_bytes(base64.b64decode(item,validate=True)) for item in state['cuda']]}


class CaseResultCache:
    def __init__(self,root,context):
        self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True)
        self.context=str(context)

    def path(self,case_id):
        digest=hashlib.sha256(_canonical([self.context,str(case_id)])).hexdigest()
        return self.root/(digest+'.json')

    def get(self,case_id,pre_rng):
        path=self.path(case_id)
        if not path.exists():return None
        envelope=json.loads(path.read_text())
        payload=envelope['payload']
        if envelope['sha256']!=hashlib.sha256(_canonical(payload)).hexdigest():
            raise ValueError('Corrupted per-case evaluation cache')
        expected=hashlib.sha256(_canonical(pre_rng)).hexdigest()
        if (payload['context']!=self.context or payload['case_id']!=str(case_id)
                or payload['schema']!='unigdnetr-case-rng-v1' or payload['pre_rng_sha256']!=expected):
            raise ValueError('Per-case cache identity or RNG chain differs')
        return _unsafe(payload['rows']),payload['post_rng']

    def put(self,case_id,pre_rng,post_rng,rows):
        if not rows:raise ValueError('Cannot cache an empty case result')
        payload={'schema':'unigdnetr-case-rng-v1','context':self.context,'case_id':str(case_id),
                 'pre_rng_sha256':hashlib.sha256(_canonical(pre_rng)).hexdigest(),
                 'post_rng':post_rng,'rows':_safe(rows)}
        envelope={'payload':payload,'sha256':hashlib.sha256(_canonical(payload)).hexdigest()}
        path=self.path(case_id);temporary=path.with_suffix(f'.{os.getpid()}.tmp')
        try:
            with temporary.open('wb') as handle:
                handle.write(_canonical(envelope));handle.flush();os.fsync(handle.fileno())
            os.replace(temporary,path)
        finally:
            if temporary.exists():temporary.unlink()
