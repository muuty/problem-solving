class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        lines = [int(9 * (10 ** (i-1)) * i) for i in range(0, 15)]
        i = 0
        _sum = 0
        while True:
            if _sum < n:
                _sum += lines[i+1]
                i += 1
                continue
            else:
                break
        remain = n - sum(lines[0: i])
        number = remain // (i)
        last = remain % (i)

        if last == 0:
            return list(str(10 ** (i-1) + number - 1))[-1]
        else:
            return list(str(10 ** (i-1) + number))[last-1]

print(Solution().findNthDigit(5))
print(Solution().findNthDigit(189))
print(Solution().findNthDigit(190))