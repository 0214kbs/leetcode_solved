class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        nums.sort()
        for t in range(1, target+1):
            for n in nums:
                if n <= t: dp[t] += dp[t-n]
            # print(dp)
        return dp[target]