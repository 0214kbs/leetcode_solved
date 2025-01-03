from collections import deque
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] >= target: return 1
        sizes= []
        l = 0
        cur = 0
        for r in range(len(nums)):
            cur += nums[r] 
            while cur >= target:
                sizes.append(r-l+1)
                cur -= nums[l]
                l +=1
        if len(sizes) == 0: return 0
        return min(sizes)