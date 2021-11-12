def dfs(answer, i, candidates, remain, result):
    if remain == 0:
        result.append(answer)
        return

    if i == len(candidates):
        return

    num = candidates[i]
    for j in range(0, remain // num + 1):
        dfs(answer + [num]*j , i + 1, candidates, remain - num * j, result)


class Solution(object):
    def combinationSum(self, candidates, target):
        answer = []
        result = []
        dfs(answer, 0, candidates, target, result)
        return result

print(Solution().combinationSum( [2,3,5], 8))