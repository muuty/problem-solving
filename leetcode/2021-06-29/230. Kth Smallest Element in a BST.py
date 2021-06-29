class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.result = -1
        def travel(node):
            if node and self.result == -1:
                travel(node.left)
                self.count += 1
                if self.count == k:
                    self.result = node.val
                    return
                travel(node.right)
        travel(root)
        return self.result

