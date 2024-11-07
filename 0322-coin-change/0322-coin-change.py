class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = int(1e9)
        if amount == 0: return 0
        dp = [INF for _ in range(amount+1)]
        dp[0] = 0

        for cur in range(1, amount+1):
            for c in coins:
                if cur-c > 0 and dp[cur-c] != INF:
                    dp[cur] = min(dp[cur-c]+1, dp[cur])
                elif cur == c: dp[cur] = 1
        print(dp)
        if dp[amount] == INF: return -1
        else: return dp[amount]