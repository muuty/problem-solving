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
        result = None
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
                new_result = (left, right)
                if result == None or result[1] - result[0] > right-left:
                    result = new_result
                left_moved = True
            else:
                right_moved = True

        if result == None:
            return ''
        return s[result[0]:result[1]]
