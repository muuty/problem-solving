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
            if i != 0 and mod_sum == 0:
                return True
            if mod_sum in mod_data and i - mod_data[mod_sum] >= 2:
                return True
            if mod_sum not in mod_data:
                mod_data[mod_sum] = i
        return False
