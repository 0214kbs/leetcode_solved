class Solution:
    def jump(self, nums: List[int]) -> int:
        INF = int(1e9)
        dp = [INF for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i+j < len(nums):
                    dp[i+j] = min(dp[i]+1, dp[i+j])
        print(dp)
        return(dp[-1])