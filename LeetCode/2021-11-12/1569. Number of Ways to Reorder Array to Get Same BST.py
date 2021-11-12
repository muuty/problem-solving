import math


def comb(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get(nums):
            if len(nums) <= 1:
                return 1
            left = [node for node in nums if node < nums[0]]
            right = [node for node in nums if node > nums[0]]
            return comb(len(left) + len(right), len(right)) * get(right) * get(left)

        return (get(nums) - 1) % (10**9 + 7)

print(Solution().numOfWays([3,1,2,5,4,6]))

