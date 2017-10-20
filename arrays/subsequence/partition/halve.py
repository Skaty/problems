'''
Problem:
Given a list of numbers, determine if it is possible
to divide the list into two subsequences
where the sum of each sublist are equal.

Assumption: Input list is never empty.
'''

def canHalve(xs):
    xs_sum = sum(xs)
    sum_to = xs_sum // 2

    if xs_sum % 2 == 1:
        return False

    # possibilities[sum][right_idx]
    possibilities = [[False] * (len(xs) + 1) for x in range(sum_to + 1)]

    # Possible to sum up to zero
    for i in range(len(xs) + 1):
        possibilities[0][i] = True

    # Fill up all possible items in DP table
    for end_idx in range(len(xs)):
        for sum_val in range(1, sum_to + 1):
            # The question is: is it possible to
            # get a subset ending at end_idx, which
            # sums up to sum_val
            # First case: We don't include current item
            possibilities[sum_val][end_idx + 1] = possibilities[sum_val][end_idx]

            # Second case: We include current item. This is only possible
            # if sum_val > xs[end_idx]!
            possibilities[sum_val][end_idx + 1] = possibilities[sum_val][end_idx + 1] or possibilities[sum_val - xs[end_idx]][end_idx]

    return possibilities[sum_to][len(xs)]

# Test cases
assert(canHalve([2,2])) # Base case
assert(canHalve([1,2,1,2])) # Positive test case
assert(canHalve([1,3]) == False) # Negative test case
assert(canHalve([-1,1,1,-1])) # Negative numbers
