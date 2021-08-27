class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(s):
            return s[::-1] == s

        def dfs(i, s, current, result):
            if i == len(s):
                return

            if is_palindrome(s[i:]):
                result.append(current + [s[i:]])

            for j in range(i + 1, len(s)):
                if is_palindrome(s[i:j]):
                    dfs(j, s, current + [s[i:j]], result)

        result = []

        dfs(0, s, [], result)
        return result




print(Solution().partition("aab"))