
class Solution(object):
    def maxEnvelopes(self, envelopes):

        n = len(envelopes)
        if n <= 1:
            return n

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        max_size = 0
        LSS = [0] * n
        for w, h in envelopes:
            l, r = 0, max_size - 1
            while l <= r :
                mid = (l+r) // 2
                if LSS[mid] >= h:
                    r = mid - 1
                else:
                    l = mid + 1

            LSS[l] = h
            max_size = max(max_size, l+1)
        return max_size



print(Solution().maxEnvelopes(
[[5,4],[6,4],[6,7],[2,3]]))








'''

Time : O(n2) -> failed on 83/84


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x:x[1])
        dp = [1 for _ in envelopes]
        answer = 1
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            answer = max(dp[i], answer)
        return answer

'''