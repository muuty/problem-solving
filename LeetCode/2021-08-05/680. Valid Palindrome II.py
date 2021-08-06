class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_palindrome(s):
            return s == s[::-1]

        left = 0
        right = len(s) - 1
        if is_palindrome(s):
            return True

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if is_palindrome(s[left+1: right+1]) or is_palindrome(s[left: right]):
                    return True
                else:
                    return False