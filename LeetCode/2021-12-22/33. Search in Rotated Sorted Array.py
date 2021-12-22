def search_pivot_point(nums):
    left = 0
    right = len(nums) - 1

    if nums[left] < nums[right]:

        return 0
    count = 0
    while left < right:
        middle = (left + right) // 2
        if count < 5:
            print(left, middle, right)
            count += 1
        if nums[left] > nums[middle]:
            right = middle

        elif nums[middle] > nums[right]:
            left = middle + 1

        elif nums[left] < nums[right]:
            return left

    return left


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    if len(nums) == 1:
        return 0 if target == nums[0] else -1

    while left <= right:
        if left == right and nums[left] != target:
            return -1

        middle = (left + right) // 2
        if target > nums[middle]:
            left = middle + 1

        elif target < nums[middle]:
            right = middle

        else:
            return middle
    return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        if len(nums) == 1:
            if target in nums:
                return 0
            return -1
        # 1 find pivot point
        # 2 two binary search
        # = 3 log(n)
        pivot_point = search_pivot_point(nums)
        print("pivot: ",pivot_point)
        if target <= nums[-1]:
            answer = binary_search(nums[pivot_point:], target)
            return -1 if answer == -1 else answer + pivot_point
        elif target >= nums[0]:
            return binary_search(nums[0:pivot_point+1], target)

        else:
            return -1

#print(Solution().search([4,5,6,7,0,1,2], 0))
#print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([4,5,6,7,0,1,2],0))
print(Solution().search([3,1],0))
