import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def count_letters(string):
            counts = collections.defaultdict(int)
            for letter in string:
                counts[letter] += 1
            return counts

        def is_included(s_counts, t_counts):
            for letter in t_counts:
                if s_counts[letter] < t_counts[letter]:
                    return False
            return True

        t_counts = count_letters(t)
        s_counts = collections.defaultdict(int)
        minimum_substring = ''
        left = 0
        right = 0

        m = len(s)
        n = len(t)

        right_moved = False
        left_moved = False
        while right < m+1:
            if right_moved:
                if right == m:
                    break
                s_counts[s[right]] += 1
                right += 1
                right_moved = False
            if left_moved:
                s_counts[s[left]] -= 1
                left += 1
                left_moved = False


            if is_included(s_counts, t_counts):
                new_substring = s[left:right]
                if minimum_substring == '' or len(minimum_substring) > len(new_substring):
                    minimum_substring = new_substring
                left_moved = True
            else:
                right_moved = True

        return minimum_substring


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a", "aa"))