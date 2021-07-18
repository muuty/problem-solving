from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()

        result = []
        self.combine(candidates, 0, [], result, target)
        return result

    def combine(self, candidates, index, path, result, target):
        if target == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue

            if candidates[i] > target:
                break

            self.combine(candidates, i+1, path + [candidates[i]], result, target - candidates[i])


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))