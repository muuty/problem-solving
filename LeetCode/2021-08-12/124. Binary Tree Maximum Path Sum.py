# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def cal_local_max_path_sum_from_node(node, global_max_value):
            if not node:
                return 0
            left_sum = cal_local_max_path_sum_from_node(node.left, global_max_value)
            right_sum = cal_local_max_path_sum_from_node(node.right, global_max_value)

            # if left - node - right is max
            center_path_sum = node.val + max(0, left_sum) + max(0, right_sum)
            if center_path_sum > global_max_value[0]:
                global_max_value[0] = center_path_sum

            return max([node.val + max(0,left_sum), node.val + max(0, right_sum)])

        max_value = [root.val]
        cal_local_max_path_sum_from_node(root, max_value)
        return max_value[0]



