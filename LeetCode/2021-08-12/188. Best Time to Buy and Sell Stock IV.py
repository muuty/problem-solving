class Solution(object):
    def maxProfit(self, k, prices):
        after_ith_buy = [-float('inf')] * k
        after_ith_sell = [0] * k
        for price in prices:
            for i in range(k):
                if i == 0:
                    after_ith_buy[i] = max(after_ith_buy[i], -price)
                else:
                    after_ith_buy[i] = max(after_ith_sell[i-1], -price)
                after_ith_sell[i] = max(after_ith_sell[i], after_ith_buy[i] + price)
        return after_ith_sell[-1]

