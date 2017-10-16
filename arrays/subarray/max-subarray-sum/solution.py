def maxSubarraySum(arr):
    global_max = current_max = arr[0]
    current_start = current_end = global_start = global_end = 0

    for idx in range(1, len(arr)):
        current_end = idx
        current_max += arr[idx]
        if current_max < arr[idx]:
            # it's better if we start from here instead
            current_start = current_end = idx
            current_max = arr[idx]

        if global_max < current_max:
            # current max is better
            global_start = current_start
            global_end = current_end
            global_max = current_max

    return arr[global_start:global_end+1]

# Testcases
assert(maxSubarraySum([-40, -10, -2, 1]) == [1])
assert(maxSubarraySum([100, -99, 1, 2, 3]) == [100])
assert(maxSubarraySum([1, 2, 3, 4, 5, -1]) == [1, 2, 3, 4, 5])
