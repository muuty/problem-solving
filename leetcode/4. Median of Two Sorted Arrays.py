class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_count = len(nums1) + len(nums2)
        half_count = total_count//2
        nums1_count = len(nums1)
        nums2_count = len(nums2)
        index1 = nums1_count // 2
        index2 = nums2_count // 2
        median = 0
        index = len(nums1) // 2
        turn = True
        while True:
            print(median)
            if turn == True:
                median = nums1[index]
                nums = nums2
            else:
                median = nums2[index]
                nums = nums1

            if len(nums) > half_count-index + 1:
                if nums[half_count-index] <= median < nums[half_count-index+1]:
                    break
                elif nums[half_count - index] > median:
                    print("incease")mkdi
                    turn = not turn
                    index = half_count - index + (len(nums) - half_count + index) // 2

                elif nums[half_count - index +1 ] < median:
                    print("decrease")
                    turn = not turn
                    index = (half_count - index)//2





        return median






print(Solution().findMedianSortedArrays([0,1,2],[3,4,5,6,7,8]))