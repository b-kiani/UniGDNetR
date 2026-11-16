# Embedded after the original evaluation functions; never changes training.
_evaluate_records_one_case = evaluate_records

def evaluate_records(model, records, task, experiment, seed, temperature=1.0,
                     mc_samples=1, missing_modalities=None, corruption=("clean",0.0),
                     case_cache_key=None):
    if not case_cache_key:
        raise RuntimeError("A complete evaluation job identity is required for case recovery.")
    cache=CaseResultCache(OUTPUT_ROOT / "results" / "evaluation_case_cache", case_cache_key)
    frames=[]
    for record in records:
        check_session_budget()
        before=pack_rng(_rng_state())
        hit=cache.get(record["case_id"], before)
        if hit is not None:
            rows,post=hit
            _restore_rng_state(unpack_rng(post,lambda raw:torch.from_numpy(np.frombuffer(raw,dtype=np.uint8).copy())))
            set_mc_dropout(model,False)
            print("REUSED VERIFIED CASE",experiment,seed,task,record["case_id"],flush=True)
            frames.append(pd.DataFrame(rows))
            continue
        frame=_evaluate_records_one_case(model,[record],task,experiment,seed,temperature,
                                         mc_samples,missing_modalities,corruption)
        cache.put(record["case_id"],before,pack_rng(_rng_state()),frame.to_dict("records"))
        frames.append(frame)
        print("SAVED EVALUATION CASE",experiment,seed,task,record["case_id"],flush=True)
    return pd.concat(frames,ignore_index=True) if frames else pd.DataFrame()
