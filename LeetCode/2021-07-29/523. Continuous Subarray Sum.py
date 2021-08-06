class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod_sum = 0
        mod_data = {}
        for i, num in enumerate(nums):
            mod_sum += num
            mod_sum = mod_sum % k
            print(mod_sum, num)
            if mod_sum in mod_data or mod:
                return True
            mod_data[mod_sum] = i
        return False

print(Solution().checkSubarraySum([23,2,4,6,7], 6))
print(Solution().checkSubarraySum([23,2,4,6,6], 7))
