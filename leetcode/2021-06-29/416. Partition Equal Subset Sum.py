class Solution(object):
    def canPartition(self, nums):
        s, n = sum(nums), len(nums)

        memo = {0: True}
        #memo : x를 만들 수 있는가?

        if s%2 != 0:
            return False

        def dfs(i, x):
            print(i,x)
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i,n):
                        #for문 :
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            break
            return memo[x]
        return dfs(0, s/2)

print(Solution().canPartition([1,2,5]))