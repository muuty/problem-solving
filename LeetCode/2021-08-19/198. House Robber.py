class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 3)

        for i in range(len(nums)-1, -1, -1):
            dp[i] = nums[i] + max(dp[i+2], dp[i+3])

        return max([dp[0], dp[1]])

print(Solution().rob([2,1,1,2]))

print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))