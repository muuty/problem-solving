from collections import defaultdict


def dfs(answer, i, nums, counts, remain, result):
    if remain == 0:
        result.append(answer)
        return

    if i == len(nums):
        return

    num = nums[i]
    for j in range(0, min([(remain // num) + 1, counts[num] + 1])):
        dfs(answer + [num] * j, i + 1, nums, counts, remain - num * j, result)


class Solution(object):
    def combinationSum(self, candidates, target):
        counts = defaultdict(int)
        for num in candidates:
            counts[num] += 1
        nums = list(counts.keys())
        answer = []
        result = []
        dfs(answer, 0, nums, counts, target, result)
        return result

print(Solution().combinationSum([10,1,2,7,6,1,5], 8))