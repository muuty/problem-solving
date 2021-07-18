class Solution(object):
    def findKthLargest(self, nums, k):

        return sorted(nums, reverse=True)[k-1]

print(Solution().findKthLargest([3,2,1,5,6,4], 2))