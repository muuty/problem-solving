class Solution(object):
    def maxValueAfterReverse(self, nums):
        original_sum = sum([abs(nums[i] - nums[i + 1])for i in range(0, len(nums) - 1)])
        no_left_max = 0
        no_right_max = 0
        for i in range(1, len(nums) -1):
            value = abs(nums[i+1] - nums[0]) - abs(nums[i] - nums[i+1])
            if value > no_left_max:
                no_left_max = value
        for i in range(1, len(nums) -1):
            value = abs(nums[-1] - nums[i]) - abs(nums[i] - nums[i+1])
            if value > no_right_max:
                no_right_max = value

        max_values = [ -nums[i] - nums[i + 1] - abs(nums[i] - nums[i + 1]) for i in range(0, len(nums) - 1)]
        min_values = [+ nums[i] + nums[i - 1] - abs(nums[i] - nums[i - 1]) for i in range(1, len(nums))]
        return max([original_sum + no_right_max,  original_sum+ no_left_max, original_sum + max(max_values) + max(min_values)])


print(Solution().maxValueAfterReverse([2,3,1,5,4]))
print(Solution().maxValueAfterReverse([2,4,9,24,2,1,10]))
print(Solution().maxValueAfterReverse([2,5,1,3,4]))
