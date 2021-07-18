import copy

class Solution(object):
    def push_next_number(self, positions):
        positions.append(1)

    def pop_and_push_next_number(self, positions,n):
        if len(positions) == 0:
            return

        previous_value = positions.pop()
        if previous_value < n:
            positions.append(previous_value + 1)
        else:
            self.pop_and_push_next_number(positions, n)

    def check_ok(self,positions):
        count = len(positions)
        for i in range(count):
            for j in range(i+1, count):
                if positions[i] == positions[j]:
                    return False

        for i in range(count):
            for j in range(i + 1, count):
                if abs(positions[i] - positions[j]) == abs(i - j):
                    return False
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        answers = []
        positions = [1]
        while True:
            if len(positions) == 0:
                break

            if self.check_ok(positions):
                if len(positions) == n:
                    answers.append(copy.deepcopy(positions))
                    self.pop_and_push_next_number(positions, n)
                else:
                    self.push_next_number(positions)
                continue
            else:
                self.pop_and_push_next_number(positions, n)

        output = [["."* (position-1) + "Q" + "."*(n -position) for position in answer] for answer in answers]
        return output



print(Solution().solveNQueens(4))