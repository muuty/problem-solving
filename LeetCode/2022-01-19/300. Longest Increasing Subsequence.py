class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [0] * len(nums)
        dp[len(nums)-1] = 1
        answer = 0
        for i in range(len(nums)-2, -1, -1):
            candidates = [dp[j] + 1 for j in range(i+1, len(nums)) if nums[j] > nums[i]]
            dp[i] = 1 if len(candidates) == 0 else max(candidates)
            answer = max([dp[i], answer])
        return answer

print(Solution().lengthOfLIS([0,1,0,3,2,3]))