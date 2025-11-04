# 🧠 Mini Research Debug

**Scenario:** You’re given a tiny behavioral experiment dataset and a script that **runs** and even plots something, but the summary numbers are **wrong**. Your job: debug the helpers and script so the outputs match the **acceptance targets** below. Then, write your own tests.

## Files
```
mini-research-debug/
├─ data/
│  └─ sessions.csv          # small, messy-ish research data
├─ analyze.py               # script (runs but has logic mistakes)
├─ helpers.py               # helper functions (tiny one-line bugs)
├─ test_student.py          # you add tests here
└─ test_instructor.py       # instructor verification (don’t change)
```

## Data dictionary (rows = participant × day session)
- `date` — YYYY-MM-DD
- `participant_id` — e.g., P01
- `condition` — Control/Treatment (inconsistent casing/spacing in file)
- `trials` — number of trials attempted
- `correct` — number of correct responses
- `rt` — mean reaction time (`"520ms"` or `"0.52s"`)
- `dropout` — fraction of trials dropped due to attrition (`"10%"` or `"0.10"`); empty means 0%
- `exclusions` — number of trials excluded for quality

## Correct math (what you should implement)
For each row:
```
dropout_frac = parse_percent(dropout)         # "10%" -> 0.10, "0.05" -> 0.05, "" -> 0.0
rt_ms        = parse_time_ms(rt)              # "520ms" -> 520.0; "0.52s" -> 520.0
cond         = normalize_condition(condition) # " control " -> "Control"; "TREATMENT" -> "Treatment"

net_trials   = max(trials - exclusions - int(trials * dropout_frac), 0)  # floor via int()
net_correct  = min(correct, net_trials)

accuracy     = net_correct / net_trials            (if net_trials > 0 else 0.0)
```
Aggregate by **condition** and by **day** using **sums**, not an average of per-row accuracies:
```
cond_accuracy = sum(net_correct) / sum(net_trials)
cond_mean_rt  = weighted mean by net_trials
```
*(The starter code averages per-row values — that’s a bug.)*

## ✅ Acceptance targets (once you fix everything)
Using the included `data/sessions.csv`:

**By condition**
- Control — net trials **217**, accuracy **0.8571428571**, mean RT **542.21 ms**
- Treatment — net trials **165**, accuracy **0.7757575758**, mean RT **558.61 ms**

**By day** (net trials, accuracy, mean RT)
- 2025-10-01 → **167**, **0.8742514970**, **557.84 ms**
- 2025-10-02 → **146**, **0.7465753425**, **562.33 ms**
- 2025-10-03 → **50**,  **0.8000000000**, **490.00 ms**
- 2025-10-04 → **19**,  **1.0000000000**, **530.00 ms**

**Grand totals**
- Net trials: **382**
- Accuracy:   **0.8219895288**
- Mean RT:    **549.29 ms**

## Your tasks
1. Run the script:
   ```bash
   python analyze.py
   ```
   Read the printed tables and compare against the targets above. What’s off?

2. Fix **helpers.py** first (each is a tiny bug):
   - `parse_percent` — wrong on `"0.05"`
   - `parse_time_ms` — wrong unit conversion for `"520ms"` vs `"0.52s"`
   - `normalize_condition` — not normalizing case/spacing
   - `net_trials` — not applying/dropout properly or clamping to 0
   - `compute_row_metrics` — mixes up where to apply dropout/exclusions

3. Fix **analyze.py**:
   - Normalize condition **before** grouping.
   - Aggregate accuracy with **sums**, and mean RT as a **weighted mean** by `net_trials`.

4. Add **at least 4 tests** in `test_student.py` that fail before your fixes and pass after.


Tip: set breakpoints inside `compute_row_metrics` and in the aggregation loops to watch the intermediate values change as you fix each bug.
