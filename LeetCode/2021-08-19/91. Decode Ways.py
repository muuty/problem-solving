class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            if 0 < int(s[i]) <= 26:
                dp[i] += dp[i+1]
            if i < len(s)-1 and int(s[i]) != 0 and 0 < int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]
#print(Solution().numDecodings("12"))
#print(Solution().numDecodings("226"))
print(Solution().numDecodings("06"))
