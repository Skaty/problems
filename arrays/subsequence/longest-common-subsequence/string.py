'''
Problem:
Given two sequences, x1 and x2, find the longest common subsequence (any one).

Suggested solutions for Longest Common Subsequence (LCS) problem.
General Idea for DP:
- If characters are the same, then we "consider" that element and recurse
- If not, then we can either remove last character from x1 or x2. Find maximum length
  from these two possibilities.
'''

def LCSString(x1, x2):
    matrix = [[0] * (len(x2) + 1) for i in range(len(x1) + 1)]

    for x1i in range(1, len(x1) + 1):
        for x2i in range(1, len(x2) + 1):
            if x1[x1i - 1] == x2[x2i - 1]:
                matrix[x1i][x2i] = 1 + matrix[x1i - 1][x2i - 1]
            else:
                # No match, second condition
                matrix[x1i][x2i] = max(matrix[x1i - 1][x2i], matrix[x1i][x2i - 1])

    x1i = len(x1)
    x2i = len(x2)
    LCSStr = ""

    # While we still have characters to go
    while matrix[x1i][x2i] != 0:
        if x1[x1i - 1] == x2[x2i - 1]:
            # Common character found!
            LCSStr = x1[x1i - 1] + LCSStr # It's not optimal
            x1i -= 1
            x2i -= 1
        elif matrix[x1i][x2i] == matrix[x1i - 1][x2i]:
            x1i -= 1
        else:
            x2i -= 1

    return LCSStr

# Testcases
assert(LCSString("", "") == "") # Base case
assert(LCSString("afg", "qwe") == "") # Negative case
assert(LCSString("abbbc", "abc") == "abc") # Positive case
assert(LCSString("aaaaa", "aaaaa") == "aaaaa") # Identical case
assert(LCSString("KaRp", "karp") == "ap") # Case sensitiveness
assert(LCSString("!@#$%^&*()kong", "!@#$%^&*()kong") == "!@#$%^&*()kong") # Character independent
