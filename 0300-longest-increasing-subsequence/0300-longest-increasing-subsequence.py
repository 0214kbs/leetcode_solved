class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        check = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            maxv = 1
            for j in range(0,i):
                if nums[i]>nums[j]: maxv = max(maxv, check[j]+1)
            check[i] = maxv
        print(check)
        return max(check)
