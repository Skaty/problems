'''
Problem:
Given a sequence of numbers, return an array containing the longest increasing subsequence.

Suggested solution for Longest Increasing Subsequence (LIS) problem.
'''
def LISLength(xs):
    longestLengths = [0] * len(xs)
    prevElement = [0] * len(xs)
    globalMaximum = 0
    bestIdx = 0

    if len(xs) == 0:
        return []

    for idx in range(len(xs)):
        maxSoFar = 0
        prevIdxSoFar = idx
        for prevIdx in range(idx):
            if xs[prevIdx] < xs[idx] and maxSoFar < longestLengths[prevIdx]:
                prevIdxSoFar = prevIdx
                maxSoFar = longestLengths[prevIdx]

        longestLengths[idx] = maxSoFar + 1
        prevElement[idx] = prevIdxSoFar

        if globalMaximum < longestLengths[idx]:
            globalMaximum = longestLengths[idx]
            bestIdx = idx

    idx = bestIdx
    curList = [xs[idx]]
    while idx != prevElement[idx]:
        idx = prevElement[idx]
        curList.append(xs[idx])

    curList.reverse()
    return curList

# Test Cases
assert(LISLength([]) == []) # Base case
assert(LISLength([1,2,3,4,5]) == [1,2,3,4,5]) # Positive test case
assert(LISLength([5,4,3,2,1]) == [5]) # Negative test case
assert(LISLength([1,4,2,5,3]) == [1,4,5]) # Interleaved
assert(LISLength([-1,5,-2,10,-2,99]) == [-1,5,10,99]) # Mixed signs
