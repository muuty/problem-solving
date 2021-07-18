class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = set(s)
        total_deletion = 0

        targets = dict()

        for letter in letters:
            count = s.count(letter)
            while count in targets and count > 0:
                count -= 1
                total_deletion += 1
            targets[count] = True

        return total_deletion

print(Solution().minDeletions("ceabaacb"))



