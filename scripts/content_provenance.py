"""Content identity and exact-artifact verification; never mutates checkpoints."""
import hashlib
import json
from pathlib import Path


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(8 * 1024**2), b''):
            digest.update(chunk)
    return digest.hexdigest()


def verify_artifacts(root, expected):
    root = Path(root).resolve()
    for relative, specification in expected.items():
        path = root / relative
        if path.is_symlink() or root not in path.resolve().parents:
            raise RuntimeError('Unsafe recovery artifact path: ' + relative)
        if not path.is_file() or path.stat().st_size != specification['bytes']:
            raise RuntimeError('Missing or resized recovery artifact: ' + relative)
        if sha256_file(path) != specification['sha256']:
            raise RuntimeError('Recovery artifact content differs: ' + relative)


class ContentProvenance:
    def __init__(self, roots, progress=None):
        self.roots = sorted([(Path(p).resolve(), name) for name, p in roots.items()],
                            key=lambda pair: -len(str(pair[0])))
        self.files = {}
        self.progress = progress

    def identity(self, path):
        path = Path(path).resolve()
        for root, name in self.roots:
            try:
                return name + '/' + path.relative_to(root).as_posix()
            except ValueError:
                pass
        raise RuntimeError('File is outside the pinned input/repair roots: ' + str(path))

    def signature(self, path):
        path = Path(path)
        identity = self.identity(path)
        # Cache is only in this process. All bytes are re-read in a new session.
        if identity not in self.files:
            before = path.stat()
            digest = sha256_file(path)
            after = path.stat()
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                raise RuntimeError('Input changed while hashing: ' + identity)
            self.files[identity] = {'path': identity, 'size': before.st_size, 'sha256': digest}
            if self.progress:
                self.progress(len(self.files), identity)
        return self.files[identity].copy()

    def manifest(self):
        return {'schema': 'unigdnetr-content-sha256-v1',
                'files': {k: self.files[k] for k in sorted(self.files)}}


def verify_content_baseline(current, prior):
    if prior.get('schema') != current.get('schema') or prior.get('files') != current.get('files'):
        raise RuntimeError('Content provenance differs from the saved session; recovery blocked.')
