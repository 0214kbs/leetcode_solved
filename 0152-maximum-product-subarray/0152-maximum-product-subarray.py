class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [[1,1] for _ in range(len(nums))]
        dp[0] = [nums[0],nums[0]]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i], nums[i] )
            dp[i][1] = min(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i], nums[i] )
        return max(dp)[0]
