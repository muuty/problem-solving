from collections import defaultdict

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [defaultdict(int) for _ in range(len(nums))]
        # diffs[diff][last]
        answer = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff] + 1
                    answer += dp[j][diff]
                else:
                    dp[i][diff] = 1
            print(dp)
        return answer

#print(Solution().numberOfArithmeticSlices([2,4,6,8,10])) # 7
#print(Solution().numberOfArithmeticSlices([7,7,7,7,7])) # 16
print(Solution().numberOfArithmeticSlices([2,2,3,4]))
#print(Solution().numberOfArithmeticSlices([0,1,2,2,2]))