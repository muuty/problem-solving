class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        c = {0: -1}
        runSum = 0

        for i, v in enumerate(nums):
            runSum += v

            runSum = runSum % k

            if runSum in c:
                if i - c[runSum] > 1:
                    return True
            else:
                c[runSum] = i

        return False
#print(Solution().checkSubarraySum([1,2,3], 5))
#print(Solution().checkSubarraySum([23,2,4,6,7],6))
print(Solution().checkSubarraySum([1,0,0],2))
#print(Solution().checkSubarraySum([23,2,6,4,7],13))