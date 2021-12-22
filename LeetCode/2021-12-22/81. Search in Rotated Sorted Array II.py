def search_pivot_point(nums):
    left = 0
    right = len(nums) - 1

    if nums[left] < nums[right]:
        return 0

    while left <= right:
        middle = left + (right - left) // 2

        if left == middle:
            return right

        while left < middle and nums[left] == nums[middle]:
            left += 1

        print(left, middle, right)
        if nums[left] < nums[right] or (nums[left] == nums[right] and left == right - 1):
            return left

        elif nums[left] > nums[middle]:
            right = middle

        elif nums[middle] >= nums[right]:
            left = middle


    return left


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    print(nums, target)
    if not nums:
        return False

    if len(nums) == 1:
        return True if target == nums[0] else False

    while left <= right:
        if left == right and nums[left] != target:
            return False

        middle = (left + right) // 2
        if target > nums[middle]:
            left = middle + 1

        elif target < nums[middle]:
            right = middle

        else:
            return True
    return True


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return False

        if len(nums) == 1:
            if target in nums:
                return True
            return False
        # 1 find pivot point
        # 2 two binary search
        # = 3 log(n)
        pivot_point = search_pivot_point(nums)
        print("pivot", pivot_point)
        if target <= nums[-1]:
            return binary_search(nums[pivot_point:], target)
        elif target >= nums[0]:
            return binary_search(nums[0:pivot_point+1], target)

        return False


# print(Solution().search([2,5,6,0,0,1,2], 3))
# print(Solution().search([2,5,6,0,0,1,2], 0))
#print(Solution().search([1,0,1,1,1],0))
print(Solution().search([1,1],2))
print(Solution().search([3,1],1))
print(Solution().search([2,2,2,3,2,2,2],3))
print(Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2))
print(Solution().search([15,16,19,20,25,1,3,4,5,7,10,14], 25))