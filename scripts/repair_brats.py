"""Fetch and verify pinned replacements for three damaged public BraTS scans."""
import hashlib
import json
import os
import time
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def prepare_brats_repairs(output_root, manifest):
    root = Path(output_root) / "data_repairs"
    root.mkdir(parents=True, exist_ok=True)
    revision = manifest["revision"]
    repo = manifest["repo_id"]
    fixed_ns = 1700000000 * 10**9

    def fetch(item):
        target = root / item["case"] / Path(item["path"]).name
        target.parent.mkdir(parents=True, exist_ok=True)

        def valid():
            return (target.is_file() and target.stat().st_size == item["size"]
                    and hashlib.sha256(target.read_bytes()).hexdigest() == item["sha256"])

        if not valid():
            url = f"https://huggingface.co/datasets/{repo}/resolve/{revision}/{item['path']}"
            partial = target.with_suffix(target.suffix + ".tmp")
            for attempt in range(3):
                try:
                    with urllib.request.urlopen(url, timeout=60) as response, partial.open("wb") as out:
                        while chunk := response.read(1024 * 1024):
                            out.write(chunk)
                    if partial.stat().st_size != item["size"]:
                        raise ValueError("Replacement download size mismatch")
                    if hashlib.sha256(partial.read_bytes()).hexdigest() != item["sha256"]:
                        raise ValueError("Replacement download SHA-256 mismatch")
                    os.replace(partial, target)
                    break
                except Exception:
                    partial.unlink(missing_ok=True)
                    if attempt == 2:
                        raise
                    time.sleep(1 + attempt)
        if not valid():
            raise RuntimeError(f"Repair verification failed: {target.name}")
        # Immutable checksum-pinned content gets a stable timestamp across VMs.
        os.utime(target, ns=(fixed_ns, fixed_ns))
        print("VERIFIED REPAIR", target.name, item["sha256"], flush=True)
        return item["case"], target

    with ThreadPoolExecutor(max_workers=4) as pool:
        paths = list(pool.map(fetch, manifest["files"]))
    by_case = {}
    for case, path in paths:
        by_case.setdefault(case, {})[path.name.removesuffix(".gz")] = path
    (Path(output_root) / "manifests" / "brats_repair_sources.json").write_text(json.dumps(manifest, indent=2))
    return by_case


def apply_brats_repairs(records, repair_cases, output_root):
    import numpy as np
    import nibabel as nib
    import copy
    records = copy.deepcopy(records)
    checks = []
    for record in records:
        case = record["subject_id"]
        if case not in repair_cases:
            continue
        originals = record["images"] + [record["mask"]]
        replacements = []
        for original_path in originals:
            original_path = Path(original_path)
            repaired = repair_cases[case][original_path.name]
            image = nib.load(repaired)
            array = np.asanyarray(image.dataobj)
            if image.shape != (240, 240, 155) or not np.isfinite(array).all():
                raise RuntimeError(f"Invalid replacement volume: {repaired.name}")
            if original_path.stat().st_size > 0:
                old = nib.load(original_path)
                if (old.shape != image.shape or not np.allclose(old.affine, image.affine, atol=1e-3)
                        or not np.array_equal(np.asanyarray(old.dataobj), array)):
                    raise RuntimeError(f"Cross-source image mismatch; refusing repair: {repaired.name}")
                same_as_original = True
            else:
                same_as_original = None
            if "-seg.nii" in repaired.name:
                if not set(np.unique(array)).issubset({0, 1, 2, 3}):
                    raise RuntimeError(f"Unexpected BraTS2023 labels: {repaired.name}")
            checks.append({"case": case, "file": repaired.name,
                           "original_empty": original_path.stat().st_size == 0,
                           "matches_nonempty_original": same_as_original})
            replacements.append(str(repaired))
            del array
        record["images"], record["mask"] = replacements[:-1], replacements[-1]
    if len(checks) != 15:
        raise RuntimeError(f"Expected 15 verified repair files, checked {len(checks)}")
    report = {"checks": checks, "empty_original_files": sum(c["original_empty"] for c in checks)}
    (Path(output_root) / "manifests" / "brats_repair_verification.json").write_text(json.dumps(report, indent=2))
    print("REPAIR VERIFICATION PASSED:", len(checks), "files across", len(repair_cases), "scans.", flush=True)
    return records
