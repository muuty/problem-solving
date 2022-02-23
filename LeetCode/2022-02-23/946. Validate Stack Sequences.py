class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        self.i = 1
        self.j = 0
        stack = [pushed[0]]

        while self.i < len(pushed):
            self.pop_if_possible(stack, popped)
            stack.append(pushed[self.i])
            self.i += 1

        self.pop_if_possible(stack, popped)

        return len(stack) == 0

    def pop_if_possible(self, stack, popped):
        while stack and self.j < len(popped) and stack[-1] == popped[self.j]:
            stack.pop()
            self.j += 1

print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
