class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True

        min_can_arrive = len(nums) - 1
        for i in range(len(nums) - 1)[::-1]:
            if i + nums[i] >= min_can_arrive:
                min_can_arrive = i
                if i == 0:
                    return True

        return False

print(Solution().canJump([0]))
#print(Solution().canJump([2,3,1,1,4]))
#print(Solution().canJump([3,2,1,0,4]))
#print(Solution().canJump([2,0]))