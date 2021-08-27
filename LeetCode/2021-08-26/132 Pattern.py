class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_increasing = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                is_increasing = True
                continue
            if is_increasing and nums[i] < nums[i-1]:
                return True
        return False

print(Solution().find132pattern())