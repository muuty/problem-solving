import collections

class Solution(object):
    def findAnagrams(self, s, p):

        def get_count_dict(s):
            freq = collections.defaultdict(int)
            for a in s:
                freq[a] += 1
            return freq

        def is_anagram(s1, s2):

            for a in s1:

                if s1[a] == s2[a]:
                    continue
                return False
            return True
        freq_p = get_count_dict(p)

        answers = []
        check_len = len(p)
        freq_s = get_count_dict(s[0: check_len-1])
        for i in range(len(s) - check_len + 1):
            freq_s[s[i+check_len-1]] += 1

            if is_anagram(freq_s, freq_p):
                answers.append(i)
            freq_s[s[i]] -= 1
        return answers


print(Solution().findAnagrams("abab","ab"))
