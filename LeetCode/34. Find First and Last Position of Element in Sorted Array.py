class Solution(object):
    def searchRange(self, nums, target):

        left = 0
        right = len(nums)
        position = -1
        while left <= right:
            middle = (left + right) // 2
            if middle > len(nums) - 1:
                break
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                position = middle
                break

        start = position
        end = position


        if position != -1:
            for i in range(0, position+1):
                if nums[position - i] != target:
                    break
                else:
                    start = position - i

            for i in range(0, len(nums) - position):
                if nums[position + i] != target:
                    break
                else:
                    end = position + i


        return [start, end]


print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([1], 1))
print(Solution().searchRange([1,2,3], 1))
print(Solution().searchRange([2,2], 3))