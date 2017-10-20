'''
Problem: Implement Quicksort
'''

def swap(xs, idx1, idx2):
    temp = xs[idx1]
    xs[idx1] = xs[idx2]
    xs[idx2] = temp

def partition(xs, start, end):
    '''
    Returns the final index of the pivot
    '''
    pivot_idx = start
    pivot_element = xs[end]

    for idx in range(start, end):
        if pivot_element > xs[idx]:
            # item larger, swap
            swap(xs, idx, pivot_idx)
            pivot_idx += 1

    swap(xs, pivot_idx, end)

    return pivot_idx

def quickSortRecursive(xs, start, end):
    if end - start < 1:
        # There's no need to sort
        return

    partition_idx = partition(xs, start, end)
    quickSortRecursive(xs, start, partition_idx - 1)
    quickSortRecursive(xs, partition_idx + 1, end)

def quickSort(xs):
    quickSortRecursive(xs, 0, len(xs) - 1)
    return xs

# Testcases
assert(quickSort([]) == []) # Base case
assert(quickSort([3,2,1]) == [1,2,3]) # Positive case
assert(quickSort([1,2,3]) == [1,2,3]) # Neutral case
assert(quickSort([5, -5, -4, 0, 4]) == [-5, -4, 0, 4, 5]) # Negative numbers
assert(quickSort([1, 3, 2, 4, 3]) == [1, 2, 3, 3, 4]) # Repeated numbers
