class Solution(object):
    def maxProfit(self, prices):
        after_buy = 0
        after_sell = 0
        for price in prices:
            after_buy = max(after_buy, -price)
            after_sell = max(after_sell, after_buy + price)

        return after_sell

print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))