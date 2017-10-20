'''
Problem:
Given an list of values, return a list containing all possible permutations
of the input list
'''

def permutations(xs):
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return [xs]

    result = []
    for idx in range(len(xs)):
        lst_of_permutations = permutations(xs[:idx] + xs[idx+1:])

        for idx2 in range(len(lst_of_permutations)):
            new_lst = [xs[idx]]
            new_lst.extend(lst_of_permutations[idx2])
            lst_of_permutations[idx2] = new_lst

        result.extend(lst_of_permutations)

    return result

# Testcases goes here
