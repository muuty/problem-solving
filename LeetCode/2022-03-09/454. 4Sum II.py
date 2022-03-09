from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        n, memory, count = len(nums1), defaultdict(int), 0
        for n1 in nums1:
            for n2 in nums2:
                memory[n1 + n2] += 1

        for n3 in nums3:
            for n4 in nums4:
                count += memory[- n3 - n4]

        return count


print(Solution().fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))
print(Solution().fourSumCount([0], [0], [0], [0]))
