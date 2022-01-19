class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        sums = [0]*(len(nums)+1)
        for i in range(len(nums)):
            sums[i+1] = sums[i] + nums[i]

        max_value = 0
        for i in range(0, len(nums) - firstLen+1):
            for j in range(0, len(nums) - secondLen+1):
                if (i > j and i-j < secondLen) or (j > i and j-i < firstLen) or i == j:
                    continue

                sum1 = sums[i + firstLen] - sums[i]
                sum2 = sums[j + secondLen] - sums[j]
                max_value = max([max_value, sum1 + sum2])

        return max_value


#print(Solution().maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1, 2))
#print(Solution().maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0],3, 2))
#print(Solution().maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4, 3))
#print(Solution().maxSumTwoNoOverlap([1,1,1,1,1,1,1,0,0,0],3, 4))

print(Solution().maxSumTwoNoOverlap([12,8,12,18,19,10,17,20,6,8,13,1,19,11,5], 3, 6))