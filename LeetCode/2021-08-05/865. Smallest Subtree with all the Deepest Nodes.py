# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def deep(root):
            if not root:
                return 0, None
            left_height, left_root = deep(root.left)
            right_height, right_root = deep(root.right)

            if left_height > right_height:
                return left_height + 1, left_root
            elif right_height > left_height:
                return right_height + 1, right_root
            else:  # left_height == right_height
                return left_height + 1, root

        return deep(root)[1]