class Solution(object):
    def maxProfit(self, prices):
        after_buy = 0
        after_sell = 0
        for price in prices:
            after_buy = max(after_buy, -price)
            after_sell = max(after_sell, after_buy + price)

        return after_sell