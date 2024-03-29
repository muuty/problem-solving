class Solution(object):
    def combinationSum4(self, nums, target):
        nums = sorted(nums)
        dp = [1] + [0] * target

        for i in range(target + 1):
            for num in nums:
                if num == i:
                    dp[i] += 1
                if num < i:
                    dp[i] += dp[i-num]
        return dp[target]


        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    combs[i] += 1
                if num < i:
                    combs[i] += combs[i - num]
        return combs[target]


