from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        output = []
        queue = deque()
        queue.append(root)
        while queue:
            level_len = len(queue)
            level_output = []
            for _ in range(level_len):
                node = queue.popleft()
                level_output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            output.append(level_output)
        return output
