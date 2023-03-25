class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX_VALUE = 10e9
        dp = [MAX_VALUE] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for num in range(coin, amount+1):
                dp[num] = min(dp[num], dp[num-coin] + 1)

        return dp[amount] if dp[amount] != MAX_VALUE else -1