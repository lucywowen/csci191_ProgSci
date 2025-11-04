# helpers.py — intentionally BUGGY to start

def parse_percent(text: str) -> float:
    """Return fraction: '10%'->0.10, '0.10'->0.10, ''->0.0
    BUG: Always divides by 100, so '0.05' becomes 0.0005.
    """
    t = (text or '').strip()
    if not t:
        return 0.0
    try:
        return float(t.strip('%')) / 100.0   # <-- BUG: only divide when '%' present
    except ValueError:
        return 0.0


def parse_time_ms(text: str) -> float:
    """Convert '520ms'->520.0; '0.52s'->520.0
    BUG: Always divides by 1000. '520ms' becomes 0.52 (wrong).
    """
    t = (text or '').strip().lower()
    if not t:
        return 0.0
    try:
        val = float(t.rstrip('ms').rstrip('s'))
    except ValueError:
        return 0.0
    # Wrong: unconditionally interpret as seconds
    return val * 1000 if t.endswith('s') else val / 1000  # <-- BUG: should not divide for 'ms'


def normalize_condition(name: str) -> str:
    """Normalize ' condition ' -> 'Condition'; 'TREATMENT' -> 'Treatment'
    BUG: only stripping; no case normalization or internal space collapse.
    """
    return (name or '').strip()  # <-- BUG: should also standardize spacing/case (e.g., title())


def net_trials(trials: int, exclusions: int, dropout_frac: float) -> int:
    """Compute net trials: max(trials - exclusions - floor(trials*dropout), 0)
    BUG: subtracts dropout fraction itself (tiny), may go negative, and doesn't clamp.
    """
    return trials - exclusions - int(dropout_frac)  # <-- BUG: should be int(trials*dropout_frac), clamp >=0


def compute_row_metrics(trials: int, correct: int, rt_text: str, dropout_text: str, exclusions: int):
    """Return dict with per-row metrics:
    {'net_trials': ..., 'net_correct': ..., 'rt_ms': ...}
    BUG: applies dropout/exclusions incorrectly to 'correct' instead of to trials.
    """
    frac = parse_percent(dropout_text)
    rt_ms = parse_time_ms(rt_text)
    # Wrong: subtract from correct, not from trials; and no clamping/cap
    net_correct = max(correct - exclusions - int(trials * frac), 0)   # <-- BUG
    net_trials_val = trials  # <-- BUG: ignores dropout/exclusions
    return {'net_trials': net_trials_val, 'net_correct': net_correct, 'rt_ms': rt_ms}
