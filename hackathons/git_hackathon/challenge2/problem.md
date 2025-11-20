# Challenge 2 – Optimize a Slow Algorithm

## Goal
Compute a **pairwise distance matrix** for a 2D list (matrix) of points.
Given shape `(n_samples, n_features)`, return an `(n_samples, n_samples)` matrix
of Euclidean distances between all pairs of rows.

The starter implementation is:
- Very slow (nested loops)
- Incorrectly indexed for non-square data
- Hard to read

## Your Tasks
- Fix correctness issues in distance computation.
- Optimize the implementation (you may use NumPy).
- Provide a small timing comparison in the console.

## Usage
The `demo()` function uses a built-in dataset. You can also load points from
`data/points4.txt` (space-separated x y per line) once you write your own loader.
