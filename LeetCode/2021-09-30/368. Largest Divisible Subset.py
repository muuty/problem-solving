class Solution(object):
	def largestDivisibleSubset(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		nums.sort()

		dp = [[0]] + [[nums[i]] for i in range(len(nums))]
		max_list = [nums[0]]
		for i in range(len(nums)-1, 0, - 1):
			max_count = 0
			new_list = dp[i]
			for j in range(i+1, len(nums) + 1):
				if dp[j][0] % dp[i][0] == 0 and max_count < len(dp[j]) + 1:
					max_count = len(dp[j]) + 1
					new_list = dp[i] + dp[j]
			dp[i] = new_list
			if len(new_list) > len(max_list):
				max_list = new_list

		return max_list



print(Solution().largestDivisibleSubset([4,8,10,240]
))
#print(Solution().largestDivisibleSubset([1,2,4,8]))
#print(Solution().largestDivisibleSubset([1,2,3]))