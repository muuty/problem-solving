class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = [[9] * (len(s)+1) for _ in range(len(s)+1)]

        for j in range(len(s)+1):
            for i in range(j, -1, -1):
                if i==j or s[i:j] == s[i:j][::-1]:
                    p[i][j] = 0
                else:
                    p[i][j] = min([p[i][k] + p[k][j] + 1 for k in range(i+1, j)])
        return p[0][len(s)]



print(Solution().minCut("aaabaa"))
print(Solution().minCut("bb"))
print(Solution().minCut("leet"))

