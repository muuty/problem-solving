from itertools import permutations

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    if int(t1) > int(t2):
        return -1
    else:
        return 1

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator))
    answer = str(int(''.join(n)))
    return answer



print(solution([3, 30, 34, 5, 9]))