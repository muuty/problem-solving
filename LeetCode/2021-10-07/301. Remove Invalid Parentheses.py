class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(s):
            s = filter(lambda x: x in '()', s)
            while '()' in s:
                s = s.replace('()', '')
            return not s

        candidates = set([s])
        while True:
            valid = filter(is_valid, candidates)
            if valid:
                return valid
            # remove i th element
            candidates = set([s[:i] + s[i+1:] for s in candidates for i in range(len(s))])


print(Solution().removeInvalidParentheses("()())()"))