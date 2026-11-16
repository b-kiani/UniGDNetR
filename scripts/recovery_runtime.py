# Embedded by build_kaggle.py after content fingerprints and split/audit creation.
# Source version pins are externally verified in Kaggle's saved Input UI and
# explicitly selected in the editor; they cannot be inferred from filenames.
LEGACY_V2_VERIFIED = False
prior_root = globals().get('resume_root')
prior_content = Path(prior_root) / 'manifests/content_provenance.json' if prior_root else None
baseline_digest = hashlib.sha256(json.dumps(RECOVERY_BASELINE, sort_keys=True).encode()).hexdigest()
if not prior_root:
    raise RuntimeError('This continuation requires a verified prior output; refuse a fresh start.')
prior_root = Path(prior_root)
prior_prepared = json.loads((prior_root / 'manifests/unigdnetr_prepared.json').read_text())
legacy_checkpoint_hashes = {
    v['sha256'] for k, v in RECOVERY_BASELINE['files'].items()
    if k.startswith('checkpoints/') and k.endswith('.pt')
}
# Every current split, repaired volume and pairing audit must still match the
# anchored V2 artifacts. Unrepaired files are identified by immutable Kaggle
# dataset versions. All current source bytes have also just been SHA-256 hashed.
for relative, spec in RECOVERY_BASELINE['files'].items():
    if (relative.startswith('data_repairs/') or relative.endswith('_splits_seed13.json')
            or relative == 'manifests/dataset_pairing_integrity_audit.csv'):
        verify_artifacts(OUTPUT_ROOT, {relative: spec})
if json.loads(json.dumps(asdict(CFG))) != prior_prepared['config']:
    raise RuntimeError('Configuration differs from prior preparation; recovery blocked.')
if prior_prepared['pipeline_revision'] != PIPELINE_REVISION:
    raise RuntimeError('Pipeline revision differs; recovery blocked.')

if prior_content.is_file():
    verify_content_baseline(CONTENT_PROVENANCE.manifest(), json.loads(prior_content.read_text()))
    receipt = prior_root / 'manifests/legacy_v2_content_migration.json'
    if receipt.is_file():
        previous_receipt = json.loads(receipt.read_text())
        if previous_receipt.get('baseline_sha256') != baseline_digest:
            raise RuntimeError('Legacy migration certificate differs; recovery blocked.')
        LEGACY_V2_VERIFIED = True
elif prior_prepared['dataset_fingerprint'] == RECOVERY_BASELINE['legacy_combined_fingerprint']:
    # Only the exact immutable V2 artifact set can establish this first migration.
    verify_artifacts(prior_root, RECOVERY_BASELINE['files'])
    LEGACY_V2_VERIFIED = True
    new_index_paths = []
    for task, task_splits in splits.items():
        for split_name, records in task_splits.items():
            matches = [Path(p) for p in prior_prepared['index_files']
                       if Path(p).name.startswith(task + '_' + split_name + '_')]
            if len(matches) != 1:
                raise RuntimeError('Ambiguous prior index for ' + task + '/' + split_name)
            name = task + '_' + split_name + '_' + records_fingerprint(records)[:12] + '.csv'
            target = OUTPUT_ROOT / 'slice_indices' / name
            shutil.copyfile(prior_root / 'slice_indices' / matches[0].name, target)
            new_index_paths.append(str(target))
    migrated = dict(prior_prepared)
    migrated.update(dataset_fingerprint=DATASET_FINGERPRINT,
                    task_dataset_fingerprints=TASK_DATASET_FINGERPRINTS,
                    index_files=new_index_paths,
                    identity_schema='unigdnetr-content-sha256-v1')
    (OUTPUT_ROOT / 'manifests/legacy_v2_prepared_original.json').write_text(json.dumps(prior_prepared, indent=2))
    (OUTPUT_ROOT / 'manifests/unigdnetr_prepared.json').write_text(json.dumps(migrated, indent=2))
    receipt = {
        'schema': 'explicit-v2-immutable-source-content-migration-v1',
        'baseline_sha256': baseline_digest,
        'source_notebook_version': RECOVERY_BASELINE['source_notebook_version'],
        'source_versions_verified_and_pinned': RECOVERY_BASELINE['source_versions'],
        'legacy_fingerprint': RECOVERY_BASELINE['legacy_combined_fingerprint'],
        'content_fingerprint': DATASET_FINGERPRINT,
        'checkpoint_bytes_unchanged': True,
        'reason': 'Legacy identity depends on volatile filesystem metadata. Original immutable source versions, exact saved artifacts, splits, repairs, audit and configuration were verified. All current source bytes now have persistent content hashes.',
    }
    (OUTPUT_ROOT / 'manifests/legacy_v2_content_migration.json').write_text(json.dumps(receipt, indent=2))
    print('EXPLICIT V2 CONTENT MIGRATION VERIFIED; original checkpoint bytes retained.', flush=True)
else:
    raise RuntimeError('Missing trusted content provenance; recovery blocked before indexing/training.')

(OUTPUT_ROOT / 'manifests/content_provenance.json').write_text(json.dumps(CONTENT_PROVENANCE.manifest(), indent=2))
print('CONTENT PROVENANCE VERIFIED:', len(CONTENT_PROVENANCE.files), 'files.', flush=True)

def legacy_checkpoint_verified(checkpoint):
    return (LEGACY_V2_VERIFIED
            and checkpoint.get('dataset_fingerprint') == RECOVERY_BASELINE['legacy_combined_fingerprint']
            and checkpoint.get('_verified_source_sha256') in legacy_checkpoint_hashes)
