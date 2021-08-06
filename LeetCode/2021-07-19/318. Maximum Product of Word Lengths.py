class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lens = [len(word) for word in words]
        word_sets = [set(list(word)) for word in words]
        max_len = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if len(word_sets[i].intersection(word_sets[j]))==0:
                    if lens[i]* lens[j] > max_len:

                        max_len = lens[i]* lens[j]

        return max_len



print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))