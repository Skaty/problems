'''
Problem:
Given two sequences, x1 and x2, find the length of the longest common subsequence.

Suggested solutions for Longest Common Subsequence (LCS) problem.
General Idea for DP:
- If characters are the same, then we "consider" that element and recurse
- If not, then we can either remove last character from x1 or x2. Find maximum length
  from these two possibilities.
'''

def LCSLength(x1, x2):
    matrix = [[0] * (len(x2) + 1) for i in range(len(x1) + 1)]

    for x1i in range(1, len(x1) + 1):
        for x2i in range(1, len(x2) + 1):
            if x1[x1i - 1] == x2[x2i - 1]:
                matrix[x1i][x2i] = 1 + matrix[x1i - 1][x2i - 1]
            else:
                # No match, second condition
                matrix[x1i][x2i] = max(matrix[x1i - 1][x2i], matrix[x1i][x2i - 1])

    return matrix[len(x1)][len(x2)]

# Testcases
assert(LCSLength("", "") == 0) # Base case
assert(LCSLength("afg", "qwe") == 0) # Negative case
assert(LCSLength("abbbc", "abc") == 3) # Positive case
assert(LCSLength("aaaaa", "aaaaa") == len("aaaaa")) # Identical case
assert(LCSLength("KaRp", "karp") == 2) # Case sensitiveness
assert(LCSLength("!@#$%^&*()kong", "!@#$%^&*()kong") == len("!@#$%^&*()kong")) # Character independent
