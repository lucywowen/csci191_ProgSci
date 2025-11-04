# analyze.py — intentionally BUGGY to start
import csv
from collections import defaultdict
from pathlib import Path

from helpers import (
    parse_percent, parse_time_ms, normalize_condition,
    net_trials, compute_row_metrics
)

DATA_PATH = Path(__file__).parent / "data" / "sessions.csv"


def load_rows(path=DATA_PATH):
    rows = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                'date': r['date'],
                'participant_id': r['participant_id'],
                'condition': r['condition'],  # BUG: not normalized here
                'trials': int(r['trials']),
                'correct': int(r['correct']),
                'rt': r['rt'],
                'dropout': r['dropout'],
                'exclusions': int(r['exclusions']),
            })
    return rows


def summarize_by_condition(rows):
    # BUGS:
    # - doesn't normalize condition labels
    # - averages per-row accuracy and RT instead of weighting by net_trials
    acc = defaultdict(list)
    rts = defaultdict(list)
    nts = defaultdict(int)

    for r in rows:
        cm = compute_row_metrics(r['trials'], r['correct'], r['rt'], r['dropout'], r['exclusions'])
        key = r['condition']  # <-- BUG: should be normalize_condition(r['condition'])
        if cm['net_trials'] > 0:
            acc[key].append(cm['net_correct'] / cm['net_trials'])
            rts[key].append(cm['rt_ms'])
            nts[key] += cm['net_trials']

    out = {}
    for k in acc:
        mean_acc = sum(acc[k]) / len(acc[k]) if acc[k] else 0.0  # <-- BUG: not weighted by trials
        mean_rt  = sum(rts[k]) / len(rts[k]) if rts[k] else 0.0  # <-- BUG: not weighted by trials
        out[k] = {'net_trials': nts[k], 'accuracy': mean_acc, 'mean_rt_ms': mean_rt}
    return out


def summarize_by_day(rows):
    # Day summary uses sums (closer to correct), but still depends on buggy helpers.
    sums = defaultdict(lambda: {'nt': 0, 'nc': 0, 'wrt': 0.0})
    for r in rows:
        cm = compute_row_metrics(r['trials'], r['correct'], r['rt'], r['dropout'], r['exclusions'])
        if cm['net_trials'] > 0:
            sums[r['date']]['nt'] += cm['net_trials']
            sums[r['date']]['nc'] += cm['net_correct']
            sums[r['date']]['wrt'] += cm['rt_ms'] * cm['net_trials']

    out = {}
    for d, v in sums.items():
        acc = (v['nc'] / v['nt']) if v['nt'] else 0.0
        mean_rt = (v['wrt'] / v['nt']) if v['nt'] else 0.0
        out[d] = {'net_trials': v['nt'], 'accuracy': acc, 'mean_rt_ms': mean_rt}
    return out


def print_summary(rows):
    cond = summarize_by_condition(rows)
    day  = summarize_by_day(rows)

    print("\nBy condition (BUGGY to start):")
    for k in sorted(cond):
        v = cond[k]
        print(f"  {k:10s}  nt={v['net_trials']:3d}  acc={v['accuracy']:.4f}  rt={v['mean_rt_ms']:.2f} ms")

    print("\nBy day (BUGGY to start):")
    for d in sorted(day):
        v = day[d]
        print(f"  {d}  nt={v['net_trials']:3d}  acc={v['accuracy']:.4f}  rt={v['mean_rt_ms']:.2f} ms")

    grand_nt = sum(v['net_trials'] for v in day.values())
    grand_nc = 0.0
    grand_w  = 0.0
    for d, v in day.items():
        grand_nc += v['accuracy'] * v['net_trials']  # this reconstructs nc fine
        grand_w  += v['mean_rt_ms'] * v['net_trials']
    grand_acc = grand_nc / grand_nt if grand_nt else 0.0
    grand_rt  = grand_w  / grand_nt if grand_nt else 0.0
    print(f"\nGrand: nt={grand_nt}  acc={grand_acc:.4f}  rt={grand_rt:.2f} ms\n")




def main():
    rows = load_rows()
    print_summary(rows)



if __name__ == "__main__":
    main()
