
class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""

		#dp[i] = min(dp[i - coins[0]], dp[i - coins[1]], dp[i - coins[2]]
		dp = [float('inf')] * (amount+1)
		dp[0] = 0
		for i in range(0, amount+1):
			for coin in coins:
				if i+coin < amount+1 and dp[i+coin] > dp[i] + 1:
					dp[i+coin] = dp[i] + 1
		if dp[amount] != float('inf'):
			return dp[amount]
		return -1