class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        distances = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                distances.append(abs(nums[i]- nums[j]))

        return sorted(distances)[k-1]


print(Solution().smallestDistancePair([1,6,1],3))