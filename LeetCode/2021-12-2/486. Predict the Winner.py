def is_p1_winner(p1_sum, p2_sum, nums, start, end):
    if start < end:
        return p1_sum >= p2_sum
    return not is_p2_winner(p1_sum + nums[start], p2_sum, nums, start + 1, end) or not is_p2_winner(p1_sum + nums[end],
                                                                                                    p2_sum, nums, start,
                                                                                                    end - 1)

def is_p2_winner(p1_sum, p2_sum, nums, start, end):
    if start < end:
        return p1_sum < p2_sum
    return not is_p1_winner(p1_sum, p2_sum + nums[start], nums, start + 1, end) or not is_p1_winner(p1_sum,
                                                                                                    p2_sum + nums[end],
                                                                                                    nums, start,

class Solution(object):
    def PredictTheWinner(self, nums):
        return is_p1_winner(0, 0, nums, 0, len(nums) - 1)
