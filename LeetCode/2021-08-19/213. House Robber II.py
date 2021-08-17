class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums):
            dp = [0] * (len(nums) + 3)
            for i in range(len(nums) - 1, -1, -1):
                dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])

            return max([dp[0], dp[1]])

        return max([rob_linear(nums[1:]), rob_linear(nums[:-1])])

#print(Solution().rob([2,3,2]))
print(Solution().rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

