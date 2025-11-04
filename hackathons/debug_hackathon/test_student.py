# test_student.py — add at least 4 tests that fail before fixes and pass after.
# Suggestions:
# - parse_percent handles '10%' and '0.05'
# - parse_time_ms handles '520ms' and '0.52s'
# - normalize_condition fixes spacing/case
# - compute_row_metrics yields expected numbers for a small example
# - summarize_by_condition/day match acceptance targets

from analyze import load_rows, summarize_by_condition, summarize_by_day
from helpers import parse_percent, parse_time_ms, normalize_condition, net_trials, compute_row_metrics

def test_parse_percent():
    # TODO: assert parse_percent('10%') == 0.10 and parse_percent('0.05') == 0.05
    pass

def test_parse_time_ms():
    # TODO: '520ms' -> 520.0 ; '0.52s' -> 520.0
    pass

def test_normalize_condition():
    # TODO: ' control ' -> 'Control' ; 'TREATMENT' -> 'Treatment'
    pass

def test_compute_row_metrics_example():
    # Example: trials=100, correct=86, rt='0.52s', dropout='10%', exclusions=2
    # net_trials = 100 - 2 - int(100*0.10) = 88
    # net_correct = min(86, 88) = 86
    # rt_ms = 520.0
    # TODO: assert dict values from compute_row_metrics match
    pass

def test_summaries_from_file():
    # TODO: after fixes, compare a couple of acceptance numbers (see README)
    # e.g., Control net_trials == 217 and accuracy ~ 0.8571428571
    pass
