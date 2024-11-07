class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0

        for cur in range(1, amount+1):
            for c in coins:
                if cur>=c: dp[cur] = min(dp[cur-c]+1, dp[cur])
        if dp[amount] == amount+1: return -1
        else: return dp[amount]