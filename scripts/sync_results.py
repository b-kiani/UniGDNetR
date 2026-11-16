"""Copy small experiment reports from downloaded Kaggle output into the repository."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("output_root", type=Path)
args = parser.parse_args()
src = args.output_root.resolve(strict=True)
dst = Path(__file__).resolve().parents[1] / "results"
marker = src / "manifests" / "unigdnetr_kaggle_session.json"
if not marker.is_file():
    raise SystemExit("Expected the UniGDNetR output folder containing manifests/unigdnetr_kaggle_session.json")

allowed = {
    "manifests": {"experiment_plan.csv", "unigdnetr_kaggle_session.json", "kaggle_environment.json", "kaggle_cohorts.json"},
    "logs": None,
    "tables": None,
    "figures": None,
    "results": None,
}
extensions = {".csv", ".json", ".png", ".svg", ".pdf", ".xlsx"}
exports = []
for sub, names in allowed.items():
    folder = src / sub
    if not folder.is_dir():
        continue
    for p in sorted(folder.rglob("*")):
        if not p.is_file() or p.is_symlink() or src not in p.resolve().parents:
            continue
        if p.suffix.lower() not in extensions or p.stat().st_size > 10 * 1024**2:
            continue
        if names is not None and p.name not in names:
            continue
        target = dst / p.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
        exports.append({"path": str(target.relative_to(dst)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
dst.mkdir(exist_ok=True)
(dst / "export_manifest.json").write_text(json.dumps({"session": json.loads(marker.read_text()), "files": exports}, indent=2))
print(f"Exported {len(exports)} small report files to {dst}")
