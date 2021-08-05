class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(d) for d in str(n)]
        size = len(nums)
        start = 0
        find = False
        for i in range(1,len(nums)):
            if nums[size-i] > nums[size - i - 1]:
                find = True
                start = size-i-1
                break
        if not find:
            return -1

        min = 10
        min_i = 0
        for i in range(start, len(nums)):
            if nums[i] > nums[start] and min > nums[i]:
                min = nums[i]
                min_i = i
        temp = nums[start]
        nums[start] = min
        nums[min_i] = temp
        new_num = (nums[:start] + [nums[start]] + sorted(nums[start+1:]))
        number=0
        for i in range(1, size+1):

            number += new_num[size-i] * 10**(i-1)

        if 2**32 - 1 <= number:
            return -1
        return number

print(2147483486 - 2**32)

print(Solution().nextGreaterElement(12))