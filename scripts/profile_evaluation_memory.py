"""Profile original and candidate HD95 on synthetic masks only, in a fresh process."""
import argparse
import ast
import json
from pathlib import Path
import resource
import time
import numpy as np
import scipy
from scipy import ndimage as ndi
from evaluation_memory import hd95_cropped_sequential
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--mode',choices=['original','candidate'],required=True)
parser.add_argument('--scenario',choices=['compact','broad'],required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
if args.mode=='original':
    notebook=json.loads((root/'notebooks/03_UniGDNetR_EVALUATE_original.ipynb').read_text())
    source=''.join(notebook['cells'][27]['source']);namespace={'np':np,'ndi':ndi}
    node=next(node for node in ast.parse(source).body if isinstance(node,ast.FunctionDef) and node.name=='hd95_binary')
    exec(compile(ast.Module(body=[node],type_ignores=[]),'original_hd95','exec'),namespace)
    metric=namespace['hd95_binary']
else:metric=hd95_cropped_sequential
shape=(192,192,128);pred=np.zeros(shape,dtype=bool);gt=pred.copy()
if args.scenario=='compact':
    pred[60:100,64:104,40:72]=True;gt[64:104,62:102,43:75]=True
else:
    pred[2:190,2:190,2:126]=True;gt[3:191,1:189,3:127]=True
    pred[50:70,50:70,40:60]=False;gt[55:75,50:70,40:60]=False
spacing=(.7,.7,3.)
start=time.perf_counter();result=metric(pred,gt,spacing);elapsed=time.perf_counter()-start
print(json.dumps({'mode':args.mode,'scenario':args.scenario,'synthetic':True,'shape':shape,
                  'spacing_mm':spacing,'hd95':result,'wall_seconds':elapsed,
                  'process_peak_rss_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
                  'numpy_version':np.__version__,'scipy_version':scipy.__version__}))
