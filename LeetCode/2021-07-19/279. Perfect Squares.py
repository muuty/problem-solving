import math
class Solution(object):
    def numSquares(self, n):
        def get_max_perfect_num_smaller_than(n):
            return int(math.sqrt(n))
        dp = [-1] * (n+1)
        dp[0] = 0
        def get_dp(n, dp):
            if dp[n] != -1:
                return dp[n]
            perfect_num = get_max_perfect_num_smaller_than(n)
            answers = []
            for i in range(1, perfect_num+1):
                count = n // (i**2)
                answers.append(get_dp(n % (i**2), dp) + count )
            dp[n] = min(answers)
            return dp[n]

        return get_dp(n, dp)




print(Solution().numSquares(13))