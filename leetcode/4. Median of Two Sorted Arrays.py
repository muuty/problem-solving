class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = nums1 + nums2
        nums.sort()


        count = len(nums)
        if count % 2 == 1:
            return nums[(count-1)//2] * 1.0
        else:
            return (nums[count//2] + nums[(count-2)//2])/2.0


print(Solution().findMedianSortedArrays([1,3], [2]))
