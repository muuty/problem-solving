from collections import defaultdict

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diffs = defaultdict(lambda: defaultdict(list))
        for i in range(1, len(nums)):
            j = i - 1
            if nums[i] - nums[j] in diffs:
                for key in diffs[nums[i] - nums[j]]:
                    if diffs[nums[i]-nums[j]][key][-1] == j:

                        diffs[nums[i] - nums[j]][key].append( i)
                        break
                else:
                    diffs[nums[i] - nums[j]][j].append(j)
                    diffs[nums[i] - nums[j]][j].append(i)
            else:
                diffs[nums[i] - nums[j]][j].append(j)
                diffs[nums[i] - nums[j]][j].append(i)

        answer = 0
        for diff in diffs:
            for start in diffs[diff]:
                array = diffs[diff][start]
                if len(array) >= 3:
                    answer +=  (len(array)-2) * (len(array)-1) //2
        return answer


print(Solution().numberOfArithmeticSlices([1,2,3,4,5,6]))
print(Solution().numberOfArithmeticSlices([-1,-2,-3]))