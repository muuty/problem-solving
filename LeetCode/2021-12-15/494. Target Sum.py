from collections import defaultdict


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [defaultdict(int) for i in range(len(nums))]

        for i in range(len(nums)):

            if i == 0:
                dp[i][nums[i]] += 1
                dp[i][-nums[i]] += 1
            else:
                for key in dp[i-1]:
                    dp[i][key + nums[i]] += dp[i-1][key]
                    dp[i][key - nums[i]] += dp[i-1][key]
        return dp[len(nums)-1][target]


#print(Solution().findTargetSumWays([1,1,1,1,1], 3))
print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
