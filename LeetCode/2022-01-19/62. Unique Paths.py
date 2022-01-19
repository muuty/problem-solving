class Solution(object):
    def uniquePaths(self, m, n):
        x = m - 1
        y = n - 1
        return comb(x+y, x)


def factorial(n):
    if n > 1:
        return factorial(n-1) * n
    return 1


def comb(a, b):
    return factorial(a) // factorial(b) // factorial(a-b)


print(Solution().uniquePaths(3,7))
