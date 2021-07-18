# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        output = [0] #root
        def dfs(node, max_val):
            if node is None:
                return
            if node.val >= max_val:
                output[0] += 1
            max_val =(node.val, max_val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        dfs(root, root.val)
        return output[0]


