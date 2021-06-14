# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution(object):
    def largestValues(self, root):
        if root is None:
            return []
        result = []
        line = [root]
        max_value = root.val
        while line:
            result.append(max_value)
            max_value = -2**31
            new_line = []
            for node in line:
                if node.left:
                    new_line.append(node.left)
                    if node.left.val > max_value:
                        max_value = node.left.val
                if node.right:
                    new_line.append(node.right)
                    if node.right.val > max_value:
                        max_value = node.right.val
            line = new_line

        return result
