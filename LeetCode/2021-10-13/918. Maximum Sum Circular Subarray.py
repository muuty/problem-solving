class Solution:
	def maxSubarraySumCircular(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		sum_ = 0

		sums = []
		nums_2x = nums + nums
		for num in nums_2x:
			sum_ += num
			sums.append(sum_)

		max_sum = -float('inf')
		for i in range(len(nums_2x)):
			for j in range(max([0,i - len(nums)]), i):
				if max_sum < sums[i] - sums[j]:
					max_sum = sums[i] - sums[j]

		return max_sum


print(Solution().maxSubarraySumCircular([3,-2,2,-3]))