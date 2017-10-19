'''
Problem:
Given a sequence of numbers, determine the length of the longest increasing
subsequence.

Suggested solution for Longest Increasing Subsequence (LIS) problem.
'''
def LISLength(xs):
    longestLengths = [0] * len(xs)
    globalMaximum = 0

    for idx in range(len(xs)):
        maxSoFar = 0
        for prevIdx in range(idx):
            if xs[prevIdx] < xs[idx]:
                maxSoFar = max(maxSoFar, longestLengths[prevIdx])

        longestLengths[idx] = maxSoFar + 1
        globalMaximum = max(globalMaximum, longestLengths[idx])

    return globalMaximum

# Test Cases
assert(LISLength([]) == 0) # Base case
assert(LISLength([1,2,3,4,5]) == 5) # Positive test case
assert(LISLength([5,4,3,2,1]) == 1) # Negative test case
assert(LISLength([1,4,2,5,3]) == 3) # Interleaved
assert(LISLength([-1,5,-2,10,-2,99]) == 4) # Mixed signs
