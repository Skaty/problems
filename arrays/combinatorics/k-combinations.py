def combinations(xs, k):
    results = []

    if len(xs) == 0 or k == 0:
        # Combination of zero stuff is nothing
        return [[]]

    for idx in range(len(xs)):
        if len(xs) - idx < k:
            break
        k_1_combinations = combinations(xs[idx+1:], k-1)
        k_combinations = [[xs[idx]] + ys for ys in k_1_combinations]

        results.extend(k_combinations)

    return results

cases = [
    [0],
    [3,1,2,3,4,5]
]
results = [combinations(x[1:], x[0]) for x in cases]
expected = [
    [[]],
    [[1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5], [1,4,5], [2,3,4], [2,3,5], [2,4,5], [3,4,5]]
]

# Testing
for tid in range(len(cases)):
    for res in results[tid]:
        assert(res in expected[tid])
