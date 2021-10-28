def factorize(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0

        primes = factorize(n)
        return sum(primes)

print(Solution().minSteps(4))

