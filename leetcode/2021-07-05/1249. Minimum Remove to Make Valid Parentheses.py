class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        parent_stack = []
        remove_list = set()
        for i, letter in enumerate(s):
            if letter == '(':
                parent_stack.append([i,letter])
            elif  letter == ')':
                if parent_stack and parent_stack[-1][1] == '(':
                    parent_stack.pop()
                else:
                    remove_list.add(i)
        for i, letter in parent_stack:
            remove_list.add(i)

        letters = []
        for i, letter in enumerate(s):
            if i not in remove_list:
                letters.append(letter)


        return ''.join(letters)


print(Solution().minRemoveToMakeValid("a)b(c)d"))