class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        answer = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            answer = max(dp[i], answer)
        return answer
        
        