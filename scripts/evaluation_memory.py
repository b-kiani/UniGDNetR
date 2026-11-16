"""Exact foreground-region definitions and sequential cropped HD95 distances."""
import numpy as np
from scipy import ndimage as ndi


def iter_task_regions(task, pred, gt, task_specs):
    if task=='brats':
        for name,labels in [('WT',[1,2,3]),('TC',[1,3]),('NETC',[1]),('SNFH',[2]),('ET',[3]),('RC',[4])]:
            yield name,(np.isin(pred,labels),np.isin(gt,labels))
    else:
        for value,name in enumerate(task_specs[task]['class_names'][1:],1):
            yield name,(pred==value,gt==value)


def hd95_cropped_sequential(pred, gt, spacing=(1.0,1.0,1.0)):
    pred,gt=np.asarray(pred,dtype=bool),np.asarray(gt,dtype=bool)
    if pred.shape!=gt.shape or pred.ndim!=3:
        raise ValueError('Matching 3D masks required for HD95')
    if not pred.any() or not gt.any():return np.nan
    crop=[]
    for axis in range(3):
        others=tuple(index for index in range(3) if index!=axis)
        occupied=np.flatnonzero(pred.any(axis=others)|gt.any(axis=others))
        crop.append(slice(max(0,int(occupied[0])-1),min(pred.shape[axis],int(occupied[-1])+2)))
    pred,gt=pred[tuple(crop)],gt[tuple(crop)]
    pred_border=pred ^ ndi.binary_erosion(pred)
    gt_border=gt ^ ndi.binary_erosion(gt)
    distances=ndi.distance_transform_edt(~gt_border,sampling=spacing)
    directed_to_gt=distances[pred_border]
    del distances
    distances=ndi.distance_transform_edt(~pred_border,sampling=spacing)
    directed_to_pred=distances[gt_border]
    del distances
    both=np.concatenate([directed_to_gt,directed_to_pred])
    return float(np.percentile(both,95)) if len(both) else 0.0
