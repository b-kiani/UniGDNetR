"""Disk-backed prediction buffers; inference arithmetic remains in the evaluator."""
from pathlib import Path
from tempfile import TemporaryDirectory
import numpy as np
import math
import shutil

class DiskPrediction:
    def __init__(self, classes, shape, directory=None):
        if len(shape)!=3 or any(int(value)<=0 for value in shape) or int(classes)<=0:
            raise ValueError('Positive 3D shape and class count required')
        self.temp = TemporaryDirectory(prefix='unigdnetr-eval-', dir=directory)
        self.shape = tuple(shape)
        self.closed = False
        self.written = np.zeros(self.shape[-1], dtype=bool)
        root = Path(self.temp.name)
        self.required_disk_bytes = math.prod(self.shape) * (4*int(classes)+4+2)
        reserve = self.required_disk_bytes + self.required_disk_bytes//5 + 64*1024**2
        if shutil.disk_usage(root).free < reserve:
            self.temp.cleanup()
            raise OSError('Insufficient free disk for one complete prediction volume and reserve')
        self.probs = np.memmap(root/'probabilities.bin', mode='w+', dtype=np.float32,
                               shape=(classes, *self.shape))
        self.entropy = np.memmap(root/'entropy.bin', mode='w+', dtype=np.float32, shape=self.shape)
        self.pred = np.memmap(root/'labels.bin', mode='w+', dtype=np.int16, shape=self.shape)

    def write(self, start, probabilities, entropy):
        probabilities, entropy = np.asarray(probabilities), np.asarray(entropy)
        count = probabilities.shape[0]
        end = start + count
        if (probabilities.shape[1:] != (self.probs.shape[0], *self.shape[:2])
                or entropy.shape != (count, *self.shape[:2]) or start < 0 or end > self.shape[-1]
                or self.written[start:end].any()):
            raise ValueError('Invalid or duplicate prediction batch')
        for index in range(count):
            self.probs[..., start+index] = probabilities[index]
            self.entropy[..., start+index] = entropy[index]
            self.pred[..., start+index] = probabilities[index].argmax(axis=0).astype(np.int16)
        self.written[start:end] = True

    def require_complete(self):
        if not self.written.all():
            raise RuntimeError('Incomplete volume prediction')

    def close(self):
        if not self.closed:
            for array in (self.probs, self.entropy, self.pred):
                array.flush()
                array._mmap.close()
            self.temp.cleanup()
            self.closed = True

    def __enter__(self):
        self.require_complete()
        return self

    def __exit__(self, *exc):
        self.close()


def chunked_ece(probs, gt, bins=15, max_voxels=250000, chunk_voxels=32768):
    """Preserve original flattened voxel sampling and 15-bin ECE convention."""
    total = int(np.prod(gt.shape))
    indices = (np.random.default_rng(13).choice(total, max_voxels, replace=False)
               if total > max_voxels else np.arange(total))
    counts = np.zeros(bins, dtype=np.int64)
    correct = np.zeros(bins, dtype=np.int64)
    confidence = np.zeros(bins, dtype=np.float64)
    edges = np.linspace(0, 1, bins+1)
    for start in range(0, len(indices), chunk_voxels):
        coordinates = np.unravel_index(indices[start:start+chunk_voxels], gt.shape)
        values = probs[(slice(None), *coordinates)]
        conf, pred, truth = values.max(axis=0), values.argmax(axis=0), gt[coordinates]
        for index, (low, high) in enumerate(zip(edges[:-1], edges[1:])):
            selected = (conf > low) & (conf <= high)
            counts[index] += selected.sum()
            correct[index] += (pred[selected] == truth[selected]).sum()
            confidence[index] += conf[selected].sum(dtype=np.float64)
    return float(sum(abs(correct[index]-confidence[index]) for index in range(bins)) / len(indices))
