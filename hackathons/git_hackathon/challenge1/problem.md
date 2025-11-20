# Challenge 1 – Fix the Broken Data Parser

## Goal
This script is supposed to:
1. Read a CSV file containing numeric values (one value per line).
2. Ignore invalid / non-numeric entries.
3. Compute and print the **mean** and **median** of the valid values.

Unfortunately, the starter code is **buggy** and incomplete.

## Your Tasks
- Fix all bugs so that the script runs without errors.
- Convert valid lines to floats; **skip** invalid ones (e.g., 'bad_line', 'NaN', empty lines).
- Implement correct functions to compute the mean and median.
- Add at least **one helper function** with a clear docstring.
- Handle the case where the file is empty or contains no valid numbers.

## Usage
```bash
python starter.py data/data1.csv
```

**Do not** use NumPy or Pandas for this challenge.
