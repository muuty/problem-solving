class Solution(object):
    def generate_answer(self, candidates, counts):
        answer = []
        for i in range(0, len(counts))
            answer += [candidates[i]] * counts[len(counts)-1-i]
        return answer

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


        answers = [(target, [])]


        for i in range(len(candidates)-1, -1, -1):
            next_answers = []
            for answer in answers:
                remain, comb = answer
                for j in range(0, remain // candidates[i]+1):
                    new_comb = comb + [j]
                    new_remain = remain - j*candidates[i]
                    next_answers.append((new_remain, new_comb))
            answers = next_answers

        answers = [answer[1] for answer in answers if answer[0] == 0]
        answers = [self.generate_answer(candidates, answer) for answer in answers]

        return answers


print(Solution().combinationSum([2,3,5], 8))
print(Solution().combinationSum([2], 1))
print(Solution().combinationSum([1], 2))