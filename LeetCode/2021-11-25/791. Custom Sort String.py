class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        custom_string = []
        for o in order:
            count = s.count(o)
            custom_string += [o] * count

        for letter in s:
            if letter not in custom_string:
                count = s.count(letter)
                custom_string += [letter] * count

        return ''.join(custom_string)

print(Solution().customSortString("kqep", "pekeq"))
