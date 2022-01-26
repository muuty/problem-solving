class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_to_letter = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        answer = ['']
        for digit in digits:
            answer = [p + q for p in answer for q in digit_to_letter[digit]]
        return answer


