import random
import bisect
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cum_weight = []
        self.total_weight = 0
        for i in w:
            self.total_weight += i
            self.cum_weight.append(self.total_weight)


    def pickIndex(self):
        """
        :rtype: int
        """
        seed = random.randint(0, self.total_weight-1)
        i = bisect.bisect_left(self.cum_weight, seed)
        return i



obj = Solution([1,3])
param_1 = obj.pickIndex()
print(param_1)