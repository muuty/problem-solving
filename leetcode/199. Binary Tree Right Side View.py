# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root:
            line = [root]
        else:
            return []
        result = []
        while line:
            result.append(line[-1].val)
            new_line = []
            for node in line:
                if node.left:
                    new_line.append(node.left)
                if node.right:
                    new_line.append(node.right)

            line = new_line

        return result
