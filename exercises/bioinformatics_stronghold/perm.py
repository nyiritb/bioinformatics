'''
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
'''

from itertools import permutations

def permutate(n: int) -> list:
    '''Return the total number of permutations of length n, followed by a list of all such permutations (in any order).
    '''
    output = ''
    perms = list(permutations(range(1, n + 1)))
    output += str(len(perms)) + '\n'
    for perm in perms:
        output += (' '.join(map(str, perm))) + '\n'
    output = output.strip()
    print(output)
    return output