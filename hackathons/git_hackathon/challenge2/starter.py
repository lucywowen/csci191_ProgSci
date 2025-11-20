import math
import time

def slow_pairwise_distances(matrix):
    """Very slow, buggy implementation of pairwise distances.

    matrix: list of lists, shape (n_samples, n_features)
    returns: list of lists, shape (n_samples, n_samples)
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0]) if n_rows > 0 else 0

    # BUGS: lots of nested loops, some indices are wrong,
    # and computation is inefficient.
    distances = [[0.0 for _ in range(n_cols)] for _ in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_cols):  # BUG: should not loop over n_cols here
            total = 0.0
            for k in range(n_cols):
                diff = matrix[i][k] - matrix[j][k]  # BUG: j indexing
                total += diff * diff
            distances[i][j] = math.sqrt(total)
    return distances

def demo():
    data = [
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 1.0],
    ]

    t0 = time.time()
    dists = slow_pairwise_distances(data)
    t1 = time.time()

    print("Slow distances:")
    for row in dists:
        print(row)
    print(f"Time taken (slow): {t1 - t0:.6f} seconds")

    # TODO: implement and call your optimized version here.

if __name__ == "__main__":
    demo()
