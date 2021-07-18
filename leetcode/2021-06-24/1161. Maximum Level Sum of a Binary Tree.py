# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        max_sum = -float("inf")
        max_level = 0
        level = 1
        level_nodes = [root]
        while level_nodes:
            level_sum = sum([node.val for node in level_nodes])
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
            next_level_nodes = [kid for node in level_nodes for kid in (node.left, node.right) if kid]
            level_nodes = next_level_nodes
        return max_level

print(Solution().maxLevelSum())