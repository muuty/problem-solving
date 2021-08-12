class Solution(object):
    def maxProfit(self, prices):
        after_first_buy = after_second_buy = -float('inf')
        after_first_sell = after_second_sell = 0
        for price in prices:
            after_first_buy = max(after_first_buy, -price)
            after_first_sell = max(after_first_sell, after_first_buy + price)
            after_second_buy = max(after_second_buy, after_first_sell - price )
            after_second_sell = max(after_second_sell, after_second_buy + price)
        return after_second_sell

