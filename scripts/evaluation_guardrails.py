"""Fail-closed patient split and full clean-evaluation coverage checks."""
import math


def patient_identity(record):
    identity = record.get('patient_id') or record.get('group_id')
    if identity is None:
        raise ValueError('Missing patient/group identity')
    return str(identity)


def validate_splits(splits):
    summary = {}
    for task, partitions in splits.items():
        seen_cases, seen_patients = set(), set()
        summary[task] = {}
        for name in ('train', 'val', 'test'):
            records = partitions[name]
            cases = [str(record['case_id']) for record in records]
            patients = {patient_identity(record) for record in records}
            if not records or len(set(cases)) != len(cases):
                raise ValueError(f'Empty or duplicate case split: {task}/{name}')
            if seen_cases.intersection(cases) or seen_patients.intersection(patients):
                raise ValueError(f'Patient/case leakage across splits: {task}/{name}')
            seen_cases.update(cases); seen_patients.update(patients)
            summary[task][name] = {'scans':len(cases),'patients':len(patients)}
    return summary


def expected_clean_keys(splits, experiments, seeds, task_specs):
    validate_splits(splits)
    expected = set()
    for experiment, config in experiments.items():
        for seed in seeds:
            for task in config.get('selected_tasks') or task_specs:
                regions = (['WT','TC','NETC','SNFH','ET','RC'] if task=='brats'
                           else task_specs[task]['class_names'][1:])
                for record in splits[task]['test']:
                    for region in regions:
                        expected.add((str(experiment),int(seed),str(task),str(record['case_id']),
                                      patient_identity(record),str(region)))
    return expected


def validate_clean_coverage(rows, splits, experiments, seeds, task_specs):
    expected = expected_clean_keys(splits, experiments, seeds, task_specs)
    observed = set()
    absent = {'both_empty':0,'missed_foreground':0,'false_positive_only':0,'hd95_nan':0}
    for row in rows:
        key = (str(row['experiment']),int(row['seed']),str(row['task']),str(row['case_id']),
               str(row['patient_id']),str(row['region']))
        if key in observed:
            raise ValueError('Duplicate clean evaluation row: '+repr(key))
        observed.add(key)
        if str(row.get('corruption'))!='clean' or float(row.get('severity',-1))!=0:
            raise ValueError('Non-clean scenario in primary results')
        if str(row.get('missing_modalities'))!='[]':
            raise ValueError('Missing-modality scenario in primary results')
        gt, pred = int(row['gt_voxels']), int(row['pred_voxels'])
        if gt<0 or pred<0:
            raise ValueError('Negative foreground count')
        absent['both_empty'] += gt==0 and pred==0
        absent['missed_foreground'] += gt>0 and pred==0
        absent['false_positive_only'] += gt==0 and pred>0
        for metric in ('dice','iou','sensitivity','precision','ece'):
            value = float(row[metric])
            should_be_nan = ((metric in ('dice','iou') and gt==0 and pred==0)
                             or (metric=='sensitivity' and gt==0)
                             or (metric=='precision' and pred==0))
            if should_be_nan:
                if not math.isnan(value):raise ValueError('Wrong absence convention: '+metric)
            elif not math.isfinite(value) or not 0<=value<=1:
                raise ValueError('Invalid clean metric: '+metric)
        hd = float(row['hd95'])
        if gt==0 or pred==0:
            if not math.isnan(hd):raise ValueError('Wrong empty-mask HD95 convention')
            absent['hd95_nan'] += 1
        elif not math.isfinite(hd) or hd<0:
            raise ValueError('Invalid HD95 for nonempty masks')
        if (gt==0) != (pred==0) and float(row['dice']) != 0:
            raise ValueError('One-empty mask must have zero Dice')
    if expected != observed:
        raise ValueError(f'Incomplete clean coverage: missing={len(expected-observed)}, unexpected={len(observed-expected)}')
    return {'expected_rows':len(expected),'observed_rows':len(observed),'absence_counts':absent,
            'split_counts':validate_splits(splits)}
